import pytest
import selenium
from pages.page_billing_9 import BillingAlertFrame9
import pytest_check as check
import logging



        
    
def test_drop_down(browser):
        billing_9 = BillingAlertFrame9(browser)
        billing_9.drop_down()

        
def test_alerts(self):
    self.base_click(ALERT)
    alert = self.driver.switch_to.alert
    check.equal(alert.text, "警告弹窗", "Alert text mismatch")
    alert.accept()

    self.base_click(CONFIRM)
    confirm = self.driver.switch_to.alert
    check.equal(confirm.text, "确认弹窗", "Confirm text mismatch")
    confirm.dismiss()

        