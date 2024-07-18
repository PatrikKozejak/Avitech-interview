from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[id="identifierId"]'
        self.next_username_button = 'div[id="identifierNext"]'
        self.password_input = 'input[name="Passwd"]'
        self.next_password_button = 'div[id="passwordNext"]'

    def navigate(self):
        self.page.goto("https://gmail.com")

    def enter_username(self, username: str):
        self.page.fill(self.username_input, username)

    def click_next_button_email(self):
        self.page.click(self.next_username_button)

    def enter_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_next_button_password(self):
        self.page.click(self.next_password_button)
