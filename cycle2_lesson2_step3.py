from selenium.webdriver.support.ui import Select
from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x1_element = browser.find_element_by_id("num1")
x1 = int(x1_element.text)
x2_element = browser.find_element_by_id("num2")
x2 = int(x2_element.text)
y = x1 + x2

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(y)) 

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()