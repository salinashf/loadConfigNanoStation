
from selenium import webdriver
from page.loginPage import LoginPage
import time
import unittest
from page.logoutPage import LogoutPage
from page.settingsPage import SettingsPage
from dotenv import load_dotenv
import os
class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(os.getenv("URL_NS"))
        cls.driver.implicitly_wait(100)
        cls.driver.maximize_window()
    def  test_1_login_valid(self):
        # carga el login
        login = LoginPage(self.driver)
        login.enter_username(os.getenv("USER"))
        login.enter_password(os.getenv("PASSWORD"))
        login.click_login()
        time.sleep(5)
    def  test_2_setting_valid(self):
        # carga el tab de home
        settings_page = SettingsPage(self.driver)
        settings_page.click_tabSettings()
        time.sleep(5)
        settings_page.click_uploadFile(os.getenv("PATH_SETTINGS"))
        settings_page.click_cancelChange()
        time.sleep(5)
    def test_3_logout_valid(self):
        logout = LogoutPage(self.driver)
        logout.click_logout()
        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
if __name__ == '__main__':
    load_dotenv()
    unittest.main()
