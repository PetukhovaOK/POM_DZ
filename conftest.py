
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse = True)
def driver(request):

    chrome_options = Options()
    options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()