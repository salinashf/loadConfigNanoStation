from selenium.webdriver.common.by import By
from locator.locators import Locators

class LogoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_xpath = Locators.logout_button_xpath

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
