from behave import *


@given('We are on the search results page')
def step_impl(context):
    context.search_results_page.go_home()


@when('We click the sort by button')
def step_impl(context):
    context.search_results_page.click_sort_by()


@when('We select the star rating filter')
def step_impl(context):
    context.search_results_page.sorting_by_price()


@then('Our results will be filtered by star rating')
def step_impl(context):
    assert context.search_results_page.verify_sorting_filter().is_displayed()


@when('We click the search by property name search filter')
def step_impl(context):
    click_property_name = context.search_results_page.property_name_search_filter()
    click_property_name.click()


@when('We type a hotel name in the search by property name search filter')
def step_impl(context):
    context.search_results_page.input_property_name().send_keys("Econo Lodge Motel Village")


@when('We click the first result in the dropdown menu')
def step_impl(context):
    context.search_results_page.click_first_option()


@then('Our results page shows the property we are interested in')
def step_impl(context):
    assert context.search_results_page.verify_property_filter().is_displayed()


@when("We click the first filter in the popular filters section")
def step_impl(context):
    context.search_results_page.click_top_filter_box()


@when("We click the second filter in the popular filters section")
def step_impl(context):
    context.search_results_page.click_second_filter_box()


@then('Our results are now filtered by these two criteria')
def step_impl(context):
    assert context.search_results_page.remove_all_filters().is_displayed()
