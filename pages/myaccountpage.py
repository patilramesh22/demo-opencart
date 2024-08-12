from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver


class MyAccountPage(BaseDriver):
    __desktop_link = (By.XPATH, "//a[text()='Desktops']")
    __mac_link = (By.XPATH, "//a[contains(text(),'Mac (1)')]")
    __price = (By.XPATH, "//span[@class='price-new']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def verify_my_account_page(self):
        act_title = self.__driver.title
        exp_title = "My Account"
        if act_title == exp_title:
            print("My account page is displayed")
            return True
        else:
            print("My account page is not displayed")
            return False

    def click_on_desktops_link(self):
        self.__driver.find_element(*self.__desktop_link).click()

    def click_on_mack_link(self):
        self.__driver.find_element(*self.__mac_link).click()

    def get_price_of_mac(self):
        price = self.__driver.find_element(*self.__price).text
        print(price)
        return True
