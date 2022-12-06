from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('We are on the Sign in page')
def step_impl(context):
    context.signin_page.go_home()


@when('We input a incorrect email')
def step_impl(context):
    input_email = context.signin_page.input_email()
    input_email.send_keys("Itfproject99")


@when('We input a password')
def step_impl(context):
    input_password = context.signin_page.input_password()
    input_password.send_keys('Itfactory@98')


@then("The 'Enter a valid email' error is present")
def step_impl(context):
    error_message = context.signin_page.invalid_email_error_message().text
    assert error_message == 'Enter a valid email.'


@then('The Sign in button is disabled')
def step_impl(context):
    sign_in_button = context.signin_page.click_sign_in_button()
    assert not sign_in_button.is_enabled()


@When('We click the Forgot password link')
def step_impl(context):
    context.signin_page.click_forgot_password()


@When('We input our accounts email address')
def step_impl(context):
    context.signin_page.input_email_to_reset_password()


@When('We click the Send request button')
def step_impl(context):
    context.signin_page.send_password_reset_request()


@Then('We get the confirmation that a password reset email was sent')
def step_impl(context):
    assert context.signin_page.confirmation_password_reset().is_displayed


@When("We input our password")
def step_impl(context):
    password = context.signin_page.input_password()
    password.send_keys("Itfactory99@")


@When('We click the display password button')
def step_impl(context):
    context.signin_page.click_show_password()


@then('Our password is now visible')
def step_impl(context):
    password = context.signin_page.my_password().get_attribute("type")
    if password == "text":
        print(f'Password is {password}')
    else:
        print("Password is not visible")


@When('We click the keep me signed in box')
def step_impl(context):
    context.signin_page.click_keep_me_signed_in()


@then('The keep me signed in box is selected')
def step_impl(context):
    assert context.signin_page.keep_me_signed_in_checkbox().is_selected()


@when('we input a correct email')
def step_impl(context):
    input_email = context.signin_page.input_email()
    input_email.send_keys('Danmicuqqq@gmail.com')


@when('We input a correct password')
def step_impl(context):
    input_password = context.signin_page.input_password()
    input_password.send_keys('Itfactory99@')


@When('We click the sign in button')
def step_impl(context):
    sign_in_button = context.signin_page.click_sign_in_button()
    sign_in_button.click()


@then('We are successfully signed in and redirected back to the home page')
def step_impl(context):
    print(context.signin_page.successful_sign_in().text)
    WebDriverWait(context.browser.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Dan']")))
    assert context.signin_page.successful_sign_in().is_displayed()
