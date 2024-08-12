from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver


class RegisterPage(BaseDriver):
    __first_name = (By.ID, "input-firstname")
    __last_name = (By.ID, "input-lastname")
    __email = (By.ID, "input-email")
    __password = (By.ID, "input-password")
    __privacy_policy = (By.XPATH, "//input[@type='checkbox' and not(@id)]")
    __continue_btn = (By.XPATH, "//button[@type='submit']")
    __login_btn = (By.XPATH, "//a[text()='Login' and @class='list-group-item']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def set_first_name(self, fname):
        self.__driver.find_element(*self.__first_name).send_keys(fname)

    def set_last_name(self, lname):
        self.__driver.find_element(*self.__last_name).send_keys(lname)

    def set_email(self, email):
        self.__driver.find_element(*self.__email).send_keys(email)

    def set_password(self, pwd):
        self.__driver.find_element(*self.__password).send_keys(pwd)

    def click_on_privacy_policy(self):
        self.__driver.find_element(*self.__privacy_policy).click()

    def click_on_continue_btn(self):
        self.__driver.find_element(*self.__continue_btn).click()

    def click_on_login_btn_from_right_column_option(self):
        self.__driver.find_element(*self.__login_btn).click()

    def register_account(self, fname, lname, email, pwd):
        self.set_first_name(fname)
        self.set_last_name(lname)
        self.set_email(email)
        self.set_password(pwd)
        self.page_scroll()
        self.click_on_privacy_policy()
        self.wait_until_element_is_clickable(*self.__continue_btn)
        self.click_on_continue_btn()

    def verify_account_is_created(self):
        actual_title = self.__driver.title
        exp_title = "Your Account Has Been Created!"
        if actual_title == exp_title:
            print("My account is created")
            return True
        else:
            print("My account is not created")
            return False
