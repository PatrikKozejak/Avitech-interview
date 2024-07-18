from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.email_page import EmailPage

scenarios('../features/level2_send_email.feature')

@given('I am logged into Gmail')
def login_to_gmail(page, credentials):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.enter_username(credentials['email'])
    login_page.click_next_button_email()
    login_page.enter_password(credentials['password'])
    login_page.click_next_button_password()
    page.wait_for_selector('div[role="button"][gh="cm"]')  # Ensure inbox is loaded

@when('I compose a new email to the contact')
def compose_new_email(page, credentials):
    email_page = EmailPage(page)
    email_page.compose_email(credentials['contact_email'], 'Test Subject', 'This is a test email body.')

@when('I send the email')
def send_email(page):
    email_page = EmailPage(page)
    email_page.page.click(email_page.send_button)

@then('the email should be in the sent folder')
def verify_email_sent(page):
    email_page = EmailPage(page)
    email_page.verify_email_sent('Test Subject', 'This is a test email body.')

@when('I log out')
def logout(page):
    email_page = EmailPage(page)
    email_page.logout()

@then('I should see the Gmail about page')
def see_about_page(page):
    expected_url = "https://www.google.com/intl/en-US/gmail/about/"
    page.wait_for_url(expected_url)
    assert page.url == expected_url, f"Expected to be on {expected_url}, but was on {page.url}"
