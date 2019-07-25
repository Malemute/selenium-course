import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(str(y))

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()