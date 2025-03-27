import pytest
import selenium
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def browser(request):
    chrome_service = Service('./chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = selenium.webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture(scope='module')
def main_page(browser):
    browser.get("http://192.168.62.254:80")
    yield browser
    print('main page closed')
    

    