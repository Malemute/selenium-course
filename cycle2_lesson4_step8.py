import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price_field = browser.find_element_by_id('price')
button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

button = browser.find_element_by_tag_name('button')

button.click()

#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(str(y))

button = browser.find_element_by_id('solve')
button.click()