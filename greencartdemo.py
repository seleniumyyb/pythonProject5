#implicit wait
#explicit wait
#pause the test for few seconds using time class
import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)


