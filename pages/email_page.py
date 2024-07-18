from playwright.sync_api import Page

class EmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.compose_button = 'div[role="button"][gh="cm"]'
        self.inbox_folder = 'div[id=":3s"]'
        self.to_field = 'input[aria-label="To recipients"]'
        self.contact_suggestion = 'div[class="aXS"]'
        self.subject_field = 'input[name="subjectbox"]'
        self.body_field = 'div[aria-label="Message Body"]'
        self.file_input = 'input[type="file"]'
        self.send_button = 'div[aria-label*="Send"][role="button"]'
        self.sent_folder_link = 'a[aria-label="Sent"]'
        self.first_email_item = 'div[gh="tl"] tr.zA.yO'  # First email in the sent folder
        self.email_detail_subject = 'h2[class="hP"]'
        self.email_detail_body = 'div[class="a3s aiL "]'
        self.profile_button = '[aria-label^="Google Account:"]'
        self.logout_button = 'a[href*="Logout"]'
        self.iframe_selector = 'iframe[name="account"]'
        self.attachment_size_preview = 'div[class="vJ"]'
        self.attachment_detail = 'span:has-text("One attachment")'
        self.attachment_download_button = 'button[aria-label="Download attachment Document.txt"]'

    def compose_email(self, to: str, subject: str, body: str):
        self.page.click(self.compose_button)
        
        # Enter part of the email address up to the @ character
        self.page.wait_for_selector(self.to_field)
        self.page.locator(self.to_field).type(to[:to.index('@')], delay=100)
        self.page.click(self.contact_suggestion)
        
        self.page.fill(self.subject_field, subject)
        self.page.fill(self.body_field, body)

    def compose_email_with_attachment(self, to: str, subject: str, body: str, attachment: str):
        self.compose_email(to, subject, body)
        self.page.set_input_files(self.file_input, attachment)
        # Wait for the attachment size preview to appear
        # Indicates that the file attachment has been fully completed before it is sent
        self.page.wait_for_selector(self.attachment_size_preview)

    def verify_email_sent(self, subject: str, body: str):
        self.page.click(self.sent_folder_link)
        self.page.wait_for_url('https://mail.google.com/mail/u/0/#sent')
        # Add a small delay to ensure the list is refreshed
        self.page.wait_for_timeout(3000)
        # Click the first instance of the email item
        first_email = self.page.locator(self.first_email_item).nth(0)
        first_email.click()
        
        email_subject_text = self.page.locator(self.email_detail_subject).inner_text()
        email_body_text = self.page.locator(self.email_detail_body).inner_text()

        assert subject in email_subject_text, f"Expected subject: {subject}, but got: {email_subject_text}"
        assert body in email_body_text, f"Expected body: {body}, but got: {email_body_text}"

    def logout(self):
        self.page.click(self.profile_button)
        # Wait for the iframe to appear and switch to it
        self.page.wait_for_selector(self.iframe_selector)
        iframe = self.page.frame(name="account")
        iframe.wait_for_selector(self.logout_button, state='visible')
        iframe.click(self.logout_button)