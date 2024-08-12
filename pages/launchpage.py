from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    __myaccount_opt = (By.XPATH, "//span[text()='My Account']")
    __register_opt = (By.XPATH, "//a[text()='Register']")
    __login_opt = (By.XPATH, "//a[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def click_on_my_account_option(self):
        self.wait_until_element_is_clickable(*self.__myaccount_opt)
        self.__driver.find_element(*self.__myaccount_opt).click()

    def click_on_register_option(self):
        self.__driver.find_element(*self.__register_opt).click()

    def click_on_login_option(self):
        self.__driver.find_element(*self.__login_opt).click()
