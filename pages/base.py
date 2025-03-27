import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Base:
    # 在conftest中定义fixture创建driver, 直接在script中的测试函数传参调用fixture中创建的driver，作为实参传入给page对象
    # 好处是非常灵活，可以自定义级别session/module/class/function
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        
    # 也可以在初始化函数中直接创建driver对象属性，坏处是它属于类，只有在创建实例的时候调用一次
    # 容易产生干扰
    
    # def __init__(self):
       # pytest的执行是在项目的根目录进行，所有的导入地址都是以pytest执行时的根目录为基准去找相对路径
        # 不能是以脚本所在的位置为相对路径
        # chrome_service = Service('./chromedriver-win64/chromedriver.exe')
        # chrome_options = Options()
        # self.driver = selenium.webdriver.Chrome(service=chrome_service, options= chrome_options)
        
    def base_visit(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        
    def base_find_element(self, loc, time=10, poll=0.5):
        wait = WebDriverWait(self.driver, timeout=time, poll_frequency=poll)
        element = wait.until(EC.presence_of_element_located(loc))
        return element
    
    def base_click(self, locator):
        self.base_find_element(locator).click()
        
    def base_input(self, locator, content):
        self.base_find_element(locator).send_keys(content)
    
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file(f"reports/{time.strftime("%Y-%m-%d_%H-%M-%S")}.png")



        
    