import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('We are on the homepage')
def step_impl(context):
    context.home_page.go_home()


@when("We accept all cookies")
def step_impl(context):
    context.home_page.accept_all_cookies_button().click()


@when('We click the logo in the top left corner')
def step_impl(context):
    context.home_page.hotels_logo().click()


@then('Page is refreshed and we remain on the homepage')
def step_impl(context):
    expected_url = 'https://ca.hotels.com/'
    assert context.browser.get_current_url() == expected_url


@given("We click the going to button")
def step_impl(context):
    context.home_page.click_going_to_filter()


@given("We type in 'Calgary'")
def step_impl(context):
    context.home_page.input_filter()


@given("We select the first option from the dropdown menu")
def step_impl(context):
    context.home_page.calgary_search_option_click()


@given("We select the date filter menu")
def step_impl(context):
    context.home_page.open_dates_filter()


@given("We select the starting date of 27 December")
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dec 27, 2022']")))
    context.home_page.select_starting_date()


@given("We select the checkout date of 30 December")
def step_impl(context):
    context.home_page.select_final_date()


@given("We click the done button under the date filter")
def step_impl(context):
    context.home_page.click_done_button()


@when('We click the travellers filter')
def step_impl(context):
    context.home_page.open_travellers_filter()


@when('We change the number of travellers to 1')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "(//*[name()='svg'][@aria-label='Decrease the number of adults in room 1'])[1]")))
    context.home_page.edit_travellers_number()


@when('We click the done button under the travellers filter')
def step_impl(context):
    context.home_page.click_travellers_done_button()


@When('We click the search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('We are redirected to a results page with the filters entered')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(EC.element_to_be_clickable((By.ID, "hotels-check-in-btn")))
    assert context.home_page.verify_redirect_to_filter_page().is_displayed()


@when('We click the english button')
def step_impl(context):
    context.home_page.region_change_button().click()


@when('We click the region tab')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'English')]")))
    context.home_page.region_dropdown_selector().click()


@when('We select Australia as our region from the dropdown menu')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='300000035']")))
    context.home_page.aus_region_selector().click()


@when('We click save')
def step_impl(context):
    time.sleep(0.5)
    context.home_page.save_region_button().click()


@then('We are redirected to the Australian website')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(EC.url_contains("/?currency=AUD"))
    expected_url = "https://au.hotels.com/?currency=AUD&eapid=35&locale=en_AU&pos=HCOM_AU&siteid=300000035&tpid=3201"
    assert context.browser.get_current_url() == expected_url


@given('We are on the Australian homepage')
def step_impl(context):
    context.home_page.go_to_aus_homepage()


@when('We select Canada as our region from the dropdown menu')
def step_impl(context):
    WebDriverWait(context.browser.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[@value='300000002']")))
    context.home_page.canada_region_selector().click()


@then('We are redirected back to the Canadian homepage')
def step_impl(context):
    expected_url = "https://ca.hotels.com/?currency=CAD&eapid=2&locale=en_CA&pos=HCOM_CA&siteid=300000002&tpid=3002"
    time.sleep(1)
    assert context.browser.get_current_url() == expected_url
