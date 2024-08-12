from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver


class LoginPage(BaseDriver):
    __myaccount_opt = (By.XPATH, "//span[text()='My Account']")
    __login_opt = (By.XPATH, "//a[text()='Login']")
    __continue_btn = (By.XPATH, "//a[text()='Continue']")
    __register_btn = (By.XPATH, "//a[text()='Register' and not(@class='dropdown-item')]")
    __email_field = (By.XPATH, "//input[@id='input-email']")
    __password_field = (By.XPATH, "//input[@id='input-password']")
    __login_btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def click_on_myaccount_option(self):
        self.__driver.find_element(*self.__myaccount_opt).click()

    def click_on_login_option(self):
        self.__driver.find_element(*self.__login_opt).click()

    def click_on_continue_btn(self):
        self.__driver.find_element(*self.__continue_btn).click()

    def click_on_register_from_right_column_option(self):
        self.__driver.find_element(*self.__register_btn).click()

    def set_email(self, email):
        self.__driver.find_element(*self.__email_field).send_keys(email)

    def set_password(self, pwd):
        self.__driver.find_element(*self.__password_field).send_keys(pwd)

    def click_on_login_btn(self):
        self.__driver.find_element(*self.__login_btn).click()
