import selenium
import selenium.webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        
    def base_find_element(self, loc, time=10, poll=0.5):
        wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll)
        element = wait.until(EC.presence_of_element_located(loc))
        return element
    

        
    