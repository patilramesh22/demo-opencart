from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.__driver = driver

    def wait_until_element_is_clickable(self, locator, value):
        wait = WebDriverWait(self.__driver, 100)
        wait.until(EC.element_to_be_clickable((locator, value)))

    def page_scroll(self):
        page_length = self.__driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length")
        match = False
        while match == False:
            last_count = page_length
            if last_count == page_length:
                page_length = "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length)"
                match = True
        return page_length
