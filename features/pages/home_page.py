from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    URL = "https://ca.hotels.com/"
    AUS_URL = "https://au.hotels.com/"

    def go_to_aus_homepage(self):
        self.driver.get(self.AUS_URL)

    def hotels_logo(self):
        logo_button_selector = (By.XPATH, "(//img[@alt='hotels logo'])[1]")
        return self.driver.find_element(*logo_button_selector)

    def region_change_button(self):
        region_button_selector = (By.XPATH, "//div[contains(text(),'English')]")
        return self.driver.find_element(*region_button_selector)

    def region_dropdown_selector(self):
        dropdown_selector = (By.ID, 'site-selector')
        return self.driver.find_element(*dropdown_selector)

    def aus_region_selector(self):
        aus_selector = (By.XPATH, "//option[@value='300000035']")
        return self.driver.find_element(*aus_selector)

    def save_region_button(self):
        save_button = (By.XPATH, "//button[normalize-space()='Save']")
        return self.driver.find_element(*save_button)

    def accept_all_cookies_button(self):
        accept_all_button = (By.XPATH, "(//button[normalize-space()='Accept All'])[1]")
        return self.driver.find_element(*accept_all_button)

    def click_going_to_filter(self):
        going_to_selector = self.driver.find_element(By.XPATH, "//button[@aria-label='Going to']")
        going_to_selector.click()

    def input_filter(self):
        going_to_selector = self.driver.find_element(By.ID, "destination_form_field")
        going_to_selector.send_keys('Calgary')

    def calgary_search_option_click(self):
        calgary_search_selector = self.driver.find_element(By.XPATH, "//button[@aria-label='Calgary Alberta, Canada']")
        calgary_search_selector.click()

    def open_dates_filter(self):
        dates_selector = self.driver.find_element(By.ID, 'date_form_field-btn')
        dates_selector.click()

    def select_starting_date(self):
        starting_date_selector = self.driver.find_element(By.XPATH, "//button[@aria-label='Dec 27, 2022']")
        starting_date_selector.click()

    def select_final_date(self):
        final_date_selector = self.driver.find_element(By.XPATH, "//button[@aria-label='Dec 30, 2022']")
        final_date_selector.click()

    def click_done_button(self):
        done_button_selector = self.driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']")
        done_button_selector.click()

    def open_travellers_filter(self):
        travellers_filter_selector = self.driver.find_element(By.XPATH, "//button[@class='uitk-menu-trigger uitk-fake-input uitk-form-field-trigger']")
        travellers_filter_selector.click()

    def edit_travellers_number(self):
        travellers_number_selector = self.driver.find_element(By.XPATH, "//div[@class='uitk-layout-flex uitk-layout-flex-flex-direction-column']//div[1]//div[1]//div[1]//button[1]//span[1]//*[name()='svg']")
        travellers_number_selector.click()

    def click_travellers_done_button(self):
        travellers_done_button = self.driver.find_element(By.XPATH, "//button[@id='traveler_selector_done_button']")
        travellers_done_button.click()

    def click_search_button(self):
        search_button_selector = self.driver.find_element(By.XPATH, "//button[@id='search_button']//*[name()='svg']")
        search_button_selector.click()

    def canada_region_selector(self):
        cad_selector = (By.XPATH, "//option[@value='300000002']")
        return self.driver.find_element(*cad_selector)

    def verify_redirect_to_filter_page(self):
        check_in_filter = (By.ID, "hotels-check-in-btn")
        return self.driver.find_element(*check_in_filter)

