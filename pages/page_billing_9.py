import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.support.select import Select
import time
import logging
import pytest_check as check


url = 'http://127.0.0.1:5500/script_9.html'
DROP_DOWN = (By.CSS_SELECTOR, ".meter-test")
ALERT = (By.CSS_SELECTOR, "input[value='alert']")
CONFIRM = (By.CSS_SELECTOR, "input[value='confirm']")
PROMPT = (By.CSS_SELECTOR, "input[value='prompt']")

class BillingAlertFrame9(Base):
    def __init__(self, driver):
        # 显示调用父类的方法，可以不写但是会依赖自动查找，不是最佳实践
        super().__init__(driver)
        self.base_visit(url)
    
    def drop_down(self):
        select = Select(self.base_find_element(DROP_DOWN))
        print(select.select_by_index(0))
        time.sleep(2)
        logging.info("drop_down test passed")
        
    # def alert_confirm_prompt(self):
    #     self.base_click(ALERT)
    #     alert = self.driver.switch_to.alert
    #     print(alert.text)
    #     assert alert.text == "警告弹窗", logging.info("alert test failed")
    #     time.sleep(2)
    #     alert.accept()
    #     logging.info("alert test passed")
        
        
    #     self.base.click(CONFIRM)
    #     confirm = self.driver.switch_to.alert
    #     assert confirm.text == "确认弹窗", logging.info("confirm test failed")
    #     time.sleep(2)
    #     confirm.dismiss()
    #     logging.info("confirm test passed")
    
    # 使用pytest-check代替断言，即使check失败依然会继续向下执行不会中断


def test_alerts(self):
    self.base_click(ALERT)
    alert = self.driver.switch_to.alert
    check.equal(alert.text, "警告弹窗", "Alert text mismatch")
    alert.accept()

    self.base_click(CONFIRM)
    confirm = self.driver.switch_to.alert
    check.equal(confirm.text, "确认弹窗", "Confirm text mismatch")
    confirm.dismiss()

    
    

