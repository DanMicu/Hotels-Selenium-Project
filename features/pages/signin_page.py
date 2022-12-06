from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://ca.hotels.com/login?"

    def input_email(self):
        email_selector = (By.ID, 'loginFormEmailInput')
        return self.driver.find_element(*email_selector)

    def input_password(self):
        password_selector = (By.ID, 'loginFormPasswordInput')
        return self.driver.find_element(*password_selector)

    def click_sign_in_button(self):
        sign_in_button_selector = self.driver.find_element(By.ID, 'loginFormSubmitButton')
        return sign_in_button_selector

    def invalid_email_error_message(self):
        invalid_email_error_selector = self.driver.find_element(By.ID, 'loginFormEmailInput-error')
        return invalid_email_error_selector

    def click_forgot_password(self):
        forgot_password_selector = self.driver.find_element(By.ID, 'loginFormForgoPwdLink')
        forgot_password_selector.click()

    def input_email_to_reset_password(self):
        input_email = self.driver.find_element(By.ID, 'reset-pwd-email')
        input_email.send_keys('Danmicuqqq@gmail.com')

    def send_password_reset_request(self):
        send_request_selector = self.driver.find_element(By.ID, 'reset-pwd-email-submit')
        send_request_selector.click()

    def confirmation_password_reset(self):
        password_reset_confirmation_selector = self.driver.find_element(By.ID, 'feedback-success')
        return password_reset_confirmation_selector

    def my_password(self):
        password = self.driver.find_element(By.ID, "loginFormPasswordInput")
        return password

    def click_show_password(self):
        show_password_selector = self.driver.find_element(By.XPATH, "//button[@class='uitk-password-visibility-button uitk-input-cta']//*[name()='svg']")
        show_password_selector.click()

    def click_keep_me_signed_in(self):
        keep_me_signed_in_button = self.driver.find_element(By.ID, "loginFormRememberMeCheck")
        keep_me_signed_in_button.click()

    def keep_me_signed_in_checkbox(self):
        checkbox = (By.ID, "loginFormRememberMeCheck")
        return self.driver.find_element(*checkbox)

    def successful_sign_in(self):
        name_top_corner_selector = self.driver.find_element(By.XPATH, "//button[normalize-space()='Dan']")
        return name_top_corner_selector
