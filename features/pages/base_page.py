

class BasePage:

    URL = ""

    def __init__(self, driver):
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

