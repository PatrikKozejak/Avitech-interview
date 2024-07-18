from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.email_page import EmailPage

scenarios('../features/level1_email_login.feature')

@given('I am on the Gmail login page')
def open_email_login_page(page):
  login_page = LoginPage(page)
  login_page.navigate()

@when('I enter a valid email')
def enter_valid_email(page, credentials):
  login_page = LoginPage(page)
  login_page.enter_username(credentials['email'])

@when('I click the next button for email')
def click_next_button_email(page):
  login_page = LoginPage(page)
  login_page.click_next_button_email()

@when('I enter a valid password')
def enter_valid_password(page, credentials):
  login_page = LoginPage(page)
  login_page.enter_password(credentials['password'])

@when('I click the next button for password')
def click_next_button_password(page):
  login_page = LoginPage(page)
  login_page.click_next_button_password()

@then('I should see the inbox')
def should_see_inbox(page):
  email_page = EmailPage(page)
  page.wait_for_selector(email_page.compose_button)
  page.wait_for_selector(email_page.inbox_folder)
  assert page.query_selector(email_page.compose_button) is not None, "Inbox not loaded"
  assert page.query_selector(email_page.inbox_folder) is not None, "Inbox not loaded"

@when('I log out')
def logout(page):
  email_page = EmailPage(page)
  email_page.logout()

@then('I should see the Gmail about page')
def see_about_page(page):
  # Check if the current URL is the expected 'about' page URL
  expected_url = "https://www.google.com/intl/en-US/gmail/about/"
  page.wait_for_url(expected_url)
  assert page.url == expected_url, f"Expected to be on {expected_url}, but was on {page.url}"