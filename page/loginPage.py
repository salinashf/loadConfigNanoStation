from selenium.webdriver.common.by import By
from locator.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        # carga las los campos  a  la clase
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(
            By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(
            By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_complete_login(self):
        Locators.check_exist_element(self.driver, By.XPATH, Locators.nameSSID)
