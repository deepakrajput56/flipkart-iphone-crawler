Feature: Fetch iPhone details from Flipkart

  Scenario: Get iPhone names and prices
    Given I open the Flipkart website
    When I search for "iPhone"
    Then I should save the iPhone list in a file and print it
