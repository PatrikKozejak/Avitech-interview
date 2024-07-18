Feature: Send Email to Contact
  Scenario: Successful email creation and sending
    Given I am logged into Gmail
    When I compose a new email to the contact
    And I send the email
    Then the email should be in the sent folder
    When I log out
    Then I should see the Gmail about page
