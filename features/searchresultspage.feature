Feature: Search results page

  Background: Opening the Search results page
    Given We are on the search results page

  Scenario: Sorting our search results by star rating
    When We click the sort by button
    And We select the star rating filter
    Then Our results will be filtered by price low to high

  Scenario: Using the search by property name search filter
    When We click the search by property name search filter
    And  We type a hotel name in the search by property name search filter
    And We click the first result in the dropdown menu
    Then Our results page shows the property we are interested in

  Scenario: Using the popular filters section on the search results page
    When We click the first filter in the popular filters section
    And  We click the second filter in the popular filters section
    Then Our results are now filtered by these two criteria

