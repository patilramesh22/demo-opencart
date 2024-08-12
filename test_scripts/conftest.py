import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urllib import request
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    pfile = Properties()
    try:
        pfile.load(open("../config.properties"))
    except:
        pfile.load(open("config.properties"))
    browser = pfile['browser']
    url = pfile['url']
    ITO = pfile['ITO']
    ETO = pfile['ETO']
    use_grid = pfile['use_grid']
    grid_url = pfile['grid_url']
    if use_grid == "no":
        if browser == 'chrome':
            browser_option = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=browser_option)
            print("Launched chrome browser in local system")
        elif browser == "firefox":
            browser_option = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=browser_option)
            print("Launched firefox browser in local system")
        else:
            browser_option = webdriver.EdgeOptions()
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=browser_option)
            print("Launched edge browser in local system")
    else:
        if browser == 'chrome':
            browser_option = webdriver.ChromeOptions()
            print("Launched chrome browser in remote system")
        elif browser == 'firefox':
            browser_option = webdriver.FirefoxOptions()
            print("Launched firefox browser in remote system")
        else:
            browser_option = webdriver.EdgeOptions()
            print("Launched edge browser in remote system")
        driver = webdriver.Remote(grid_url, options=browser_option)
    driver.maximize_window()
    driver.implicitly_wait(ITO)
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()