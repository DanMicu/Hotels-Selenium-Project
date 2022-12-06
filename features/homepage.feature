Feature: Homepage

  Scenario: Clicking the hotels logo refreshes the page but doesnt change the url
    Given We are on the homepage
    When We click the logo in the top left corner
    Then Page is refreshed and we remain on the homepage

  Scenario: Searching for a hotel room in Calgary Canada for a select number of nights
    Given We are on the homepage
    And We click the going to button
    And We type in 'Calgary'
    And We select the first option from the dropdown menu
    And We select the date filter menu
    And We select the starting date of 27 December
    And We select the checkout date of 30 December
    And We click the done button under the date filter
    When We click the travellers filter
    And We change the number of travellers to 1
    And We click the done button under the travellers filter
    And We click the search button
    Then We are redirected to a results page with the filters entered

  Scenario: Changing the region displayed on the website
    Given We are on the homepage
    When We click the english button
    And We click the region tab
    And We select Australia as our region from the dropdown menu
    And We click save
    Then We are redirected to the Australian website

  Scenario: Changing the region back to Canada
    Given We are on the Australian homepage
    When We click the english button
    And We click the region tab
    And We select Canada as our region from the dropdown menu
    And We click save
    Then We are redirected back to the Canadian homepage

