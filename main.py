from locator.locators import Locators
from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
from page.loginPage import LoginPage
from page.logoutPage import LogoutPage
from page.settingsPage import SettingsPage
from dotenv import load_dotenv
import argparse
import os
import sys


class LoadConfigNS:

    def __init__(self):

        # Ruta local al geckodriver
        service = Service(os.getenv("PATH_DRIVE_FIREFOX"))
        self.driver = webdriver.Firefox(service=service)
        # Abrir la URL desde variable de entorno
        self.driver.get(os.getenv("URL_NS"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.check_load_login()

    def check_load_login(self):
        # Verifica si la pag login se cargo,  buscado un campo que exista
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, Locators.login_button_xpath)))

    def login(self, username, password):
        print("Iniciando sesión...")
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        login.check_complete_login()

    def update_settings(self, file_path):
        print("Actualizando configuración...")
        settings_page = SettingsPage(self.driver)
        settings_page.click_tabSettings()
        settings_page.check_complete_settings()
        settings_page.click_uploadFile(file_path)
        settings_page.check_complete_upload_file()
        settings_page.click_confirmChange()
        time.sleep(5)

    def logout(self):
        print("Cerrando sesión...")
        logout = LogoutPage(self.driver)
        print("Cerrando Session ...")
        logout.click_logout()
        self.check_load_login()
        print("Session Cerrada ...")

    def close_driver(self):
        print("Finalizando prueba...")
        self.driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Este script permite cargar la configuracion de NanoStation")
    parser.add_argument("-m", "--mode", type=str, help="El modo de operación del script 'Dia' o 'Noche'", required=True)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    v_mode = args.mode
    if v_mode not in ["Dia", "Noche"]:
        print("El modo de operación debe ser 'Dia' o 'Noche'")
        parser.print_help(sys.stderr)
    print(f"Modo de operación: {v_mode}")
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()
    v_path = os.getenv("PATH_SETTINGS")
    v_path = v_path.replace("{{MODE}}", v_mode)
    os.environ["PATH_SETTINGS"] = v_path
    print("La configuracion que cargaremos es: " + os.getenv("PATH_SETTINGS"))

    ldConfigNS = LoadConfigNS()
    try:
        ldConfigNS.login(os.getenv("USER"), os.getenv("PASSWORD"))
        ldConfigNS.update_settings(os.getenv("PATH_SETTINGS"))
        ldConfigNS.logout()
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        ldConfigNS.close_driver()
