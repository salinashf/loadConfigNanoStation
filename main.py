from selenium import webdriver
import time
from page.loginPage import LoginPage
from page.logoutPage import LogoutPage
from page.settingsPage import SettingsPage
from dotenv import load_dotenv
import os


class LoadConfigNS:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(os.getenv("URL_NS"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)

    def login(self, username, password):
        print("Iniciando sesión...")
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        time.sleep(5)

    def update_settings(self, file_path):
        print("Actualizando configuración...")
        settings_page = SettingsPage(self.driver)
        settings_page.click_tabSettings()
        time.sleep(5)
        settings_page.click_uploadFile(file_path)
        time.sleep(5)
        settings_page.click_confirmChange()
        time.sleep(5)

    def logout(self):
        print("Cerrando sesión...")
        logout = LogoutPage(self.driver)
        logout.click_logout()
        time.sleep(15)

    def close_driver(self):
        print("Finalizando prueba...")
        self.driver.quit()


if __name__ == "__main__":
    load_dotenv()
    ldConfigNS = LoadConfigNS()
    try:
        ldConfigNS.login(os.getenv("USER"), os.getenv("PASSWORD"))
        ldConfigNS.update_settings(os.getenv("PATH_SETTINGS"))
        ldConfigNS.logout()
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        ldConfigNS.close_driver()
