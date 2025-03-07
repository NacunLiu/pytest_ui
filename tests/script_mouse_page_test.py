import selenium
import selenium.webdriver
import selenium.webdriver.chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_service = Service('./chromedriver-win64/chromedriver.exe')
chrome_options = Options()

try:
    driver = selenium.webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    print(f'get connection failed as {e}')

driver.get("http://192.168.62.254:80")
driver.maximize_window()
time.sleep(3)
current_window = driver.current_window_handle

wait = WebDriverWait(driver, 10, 1)
actions = ActionChains(driver)

mouse_keyboard = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "mouse")))
actions.move_to_element(mouse_keyboard).perform()

time.sleep(3)
print(mouse_keyboard.text)

mouse_page_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Mouse")))
print(mouse_page_link.text)

actions.click(mouse_page_link).perform()

time.sleep(3)


window_handles = driver.window_handles
for handle in window_handles:
    if handle != current_window:
        driver.switch_to.window(handle)
time.sleep(3)

bx = wait.until(EC.presence_of_element_located((By.ID, 'draggable')))
initial_x = bx.location['x']
initial_y = bx.location['y']
bacc = bx.value_of_css_property('background-color')
print(bacc, initial_x, initial_y)

actions.click_and_hold(bx).perform()
time.sleep(3)
new_bacc = bx.value_of_css_property('background-color')

print(new_bacc, type(new_bacc))
assert new_bacc == "rgba(255, 0, 0, 1)",  f'color does not change to red when click and hold'

actions.release()

time.sleep(1)

actions.drag_and_drop_by_offset(bx, 1000, 200).perform()

time.sleep(3)

new_x = bx.location['x']
new_y = bx.location['y']

print(new_x, new_y)
assert new_x == 1010 and new_y == 210, 'Error: element does not move as expected'


driver.close()