import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(str(y))

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_css_selector("[value='robots']")
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
option1.click()

#button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()