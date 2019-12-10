Feature: Smoke Test

  Scenario: Smoke Test
    Given I start the app
    When I see Welcome page
    Then I click Signin button
    And I see Login page
    And I login to app
    Then I see Videos page

#    When I see login page
#    Then I login to app
#    And I see home page