from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    URL = "https://ca.hotels.com/Hotel-Search?destination=Calgary&regionId=4132&latLong=51.04832,-114.06999&selected=&d1=2022-12-27&startDate=2022-12-27&d2=2022-12-30&endDate=2022-12-30&adults=1"

    def click_sort_by(self):
        sort_by_selector = self.driver.find_element(By.XPATH, "//div[@class='uitk-field uitk-field-select-field has-floatedLabel-label has-no-placeholder']")
        sort_by_selector.click()

    def sorting_by_price(self):
        sorting_by_price_selector = self.driver.find_element(By.XPATH, "//option[@value='PROPERTY_CLASS']")
        sorting_by_price_selector.click()

    def verify_sorting_filter(self):
        sorting_filter_displayed_selector = (By.XPATH, "//span[@class='uitk-pill-text']")
        return self.driver.find_element(*sorting_filter_displayed_selector)

    def property_name_search_filter(self):
        property_name_filter_selector = (By.XPATH, "//div[@class='uitk-menu-trigger']//div[@class='uitk-field has-floatedLabel-label has-icon has-no-placeholder']")
        return self.driver.find_element(*property_name_filter_selector)

    def input_property_name(self):
        input_property_name = (By.XPATH, "//input[@placeholder='e.g. Marriott']")
        return self.driver.find_element(*input_property_name)

    def click_first_option(self):
        property_name_filter_selector = self.driver.find_element(By.XPATH, "//button[@aria-label='Econo Lodge Motel Village Calgary, Alberta, Canada']")
        property_name_filter_selector.click()

    def verify_property_filter(self):
        property_filter = self.driver.find_element(By.XPATH, "//header[@class='uitk-card-featured-header uitk-card-roundcorner-top-right uitk-card-roundcorner-top-left']")
        return property_filter

    def click_top_filter_box(self):
        top_filter_box_selector = self.driver.find_elements(By.XPATH, "//h4[contains(text(), 'Popular filters')]//ancestor::fieldset//input")[0]
        top_filter_box_selector.click()

    def click_second_filter_box(self):
        second_filter_box_selector = self.driver.find_elements(By.XPATH, "//h4[contains(text(), 'Popular filters')]//ancestor::fieldset//input")[1]
        second_filter_box_selector.click()

    def remove_all_filters(self):
        filter_remove_selector = (By.XPATH, "//button[normalize-space()='Remove all filters']")
        return self.driver.find_element(*filter_remove_selector)

