
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators():
    # para el login
    username_textbox_id = "username"
    password_textbox_id = "password"
    login_button_xpath = "/html/body/table/tbody/tr[2]/td[2]/input"
    nameSSID = "//*[@id='apssidstr']"
    alert_message_login_xpath = "//*[@id='errmsg']"
    # para el tab settings
    settings_tab_xpath = '/html/body/table/tbody/tr[2]/td[1]/a[6]'
    upload_file_button_xpath = '/html/body/table/tbody/tr[3]/td/form[8]/table/tbody/tr[3]/td[2]/input'
    load_settings_button_xpath = '/html/body/table/tbody/tr[3]/td/form[8]/table/tbody/tr[4]/td[2]/input'
    confirm_settings_button_xpath = '/html/body/table/tbody/tr[3]/td/div[1]/table/tbody/tr/td[2]/input[1]'
    cancel_settings_button_xpath = '/html/body/table/tbody/tr[3]/td/div[1]/table/tbody/tr/td[2]/input[2]'
    confirm_cancel_settings_button_xpath = "/html/body/form/table/tbody/tr[2]/td[2]/input"
    close_cancel_windows_settings_button_xpath = "/html/body/table/tbody/tr[6]/td/input"
    logout_button_xpath = "/html/body/table/tbody/tr[2]/td[2]/input"

    def check_exist_element(driver, by, value, timeout=10):
        try:

            elem = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(
                    (by, value)))
            return elem
        except TimeoutException:
            return None
