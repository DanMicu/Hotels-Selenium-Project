from browser import Browser
from pages.home_page import HomePage
from pages.search_results_page import SearchResultPage
from pages.signin_page import SignInPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage(context.browser.driver)
    context.signin_page = SignInPage(context.browser.driver)
    context.search_results_page = SearchResultPage(context.browser.driver)


def after_all(context):
    context.browser.close()
