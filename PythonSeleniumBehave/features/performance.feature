Feature: Performance analysis

  Scenario: Login to app
    Given I start the app
    When I see Welcome page
    Then I click Signin button
    And I see Login page
    And I login to app
    Then I see Videos page

  Scenario: Videos page performance
  	Then I navigate to Datasets page
    When I see Datasets page
    Then I navigate to Videos page 0 and check load time
    Then I navigate to Videos page "3"
    Then I navigate to Videos page 4 and check load time
    Then I navigate to Datasets page 0 and check load time
  	#Then I navigate to Videos 0 page
  	#Then I navigate to Datasets page
  	#Then I navigate to Videos 0 page



   