from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\Users\\kanti\\Downloads\\firefoxgecko64\\geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("kanti")                      NAME LOCATOR METHOD
driver.find_element_by_css_selector("input[name='name']").send_keys("rahul")    # CSS METHOD
driver.find_element_by_name("email").send_keys("shetty")                      #NAME METHOD
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(0)

#driver.find_element_by_xpath("//input[@type='submit']").click()                 XPATH METHOD
driver.find_element_by_css_selector("input[value='Submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
#print(driver.find_element_by_css_selector("[class*='alert-success']").text)       #CSS METHOD 2ND FORMULA
#print(driver.find_element_by_xpath("//*contains(@class='alert-success']").text)
#assert "success" in message