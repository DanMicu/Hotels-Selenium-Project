Feature: Sign in Page

  Background: Opening the Sign in page
    Given We are on the Sign in page

  Scenario: Sign in attempt with invalid email and password
    When We input a incorrect email
    And We input a password
    Then The 'Enter a valid email' error is present
    And The Sign in button is disabled

  Scenario: Forgot Password
    When We click the Forgot password link
    And We input our accounts email address
    And We click the Send request button
    Then We get the confirmation that a password reset email was sent

  Scenario: Verify that password we input is hidden
    When we input a correct email
    When We input our password
    When We click the display password button
    Then Our password is now visible

  Scenario: Verify that the Keep me signed in box is selected
    When we input a correct email
    And We input our password
    And We click the keep me signed in box
    Then The keep me signed in box is selected

  Scenario: Successful sign in
    When we input a correct email
    And We input a correct password
    When We click the sign in button
    Then We are successfully signed in and redirected back to the home page


