from selenium.webdriver.support.ui import WebDriverWait
from locator.locators import Locators
from selenium.webdriver.common.by import By
class SettingsPage():
    def __init__(self, driver):
        self.driver = driver
        self.settings_tab_xpath = Locators.settings_tab_xpath
        self.upload_file_button_xpath = Locators.upload_file_button_xpath
        self.load_settings_button_xpath = Locators.load_settings_button_xpath
        self.confirm_settings_button_xpath = Locators.confirm_settings_button_xpath
        self.cancel_settings_button_xpath = Locators.cancel_settings_button_xpath
        self.confirm_cancel_settings_button_xpath = Locators.confirm_cancel_settings_button_xpath
        self.close_cancel_windows_settings_button_xpath = Locators.close_cancel_windows_settings_button_xpath
    def click_tabSettings(self):
        self.driver.find_element(By.XPATH, self.settings_tab_xpath).click()

    def click_uploadFile(self, fileUpload):
        btnUpload = self.driver.find_element( By.XPATH, self.upload_file_button_xpath)
        btnUpload.send_keys(fileUpload)  # Ruta del archivo a subir
        self.driver.find_element(By.XPATH, self.load_settings_button_xpath).click()
    def click_cancelChange(self):

        original_window = self.driver.current_window_handle
        self.driver.find_element(
            By.XPATH, self.cancel_settings_button_xpath).click()

        # Espera hasta que aparezca una nueva ventana
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1)

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        # confirma la cancelación
        self.driver.find_element(
            By.XPATH, self.confirm_cancel_settings_button_xpath).click()
        # Cierra la ventana emergente
        self.driver.find_element(
            By.XPATH, self.close_cancel_windows_settings_button_xpath).click()

    def click_confirmChange(self):

        original_window = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, self.confirm_settings_button_xpath).click()

        # Espera hasta que aparezca una nueva ventana
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
