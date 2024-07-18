Feature: Email Login and Logout
  Scenario: Successful login and logout of Gmail
    Given I am on the Gmail login page
    When I enter a valid email
    And I click the next button for email
    And I enter a valid password
    And I click the next button for password
    Then I should see the inbox
    When I log out
    Then I should see the Gmail about page
