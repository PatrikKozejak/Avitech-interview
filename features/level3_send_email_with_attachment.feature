Feature: Send an Email with an Attachment to Contact
  Scenario: Send an email with an attachment and verify it
    Given I am logged into Gmail
    When I compose a new email to the contact with an attachment
    And I send the email
    Then the email should be in the sent folder with the attachment
    When I log out
    Then I should see the Gmail about page
