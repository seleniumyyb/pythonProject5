#from select import select
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("kanti")                      NAME LOCATOR METHOD
driver.find_element_by_css_selector("input[name='name']").send_keys("KANTI")    # CSS METHOD
driver.find_element_by_name("email").send_keys("PRAJAPATI")                      #NAME METHOD
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

#driver.find_element_by_xpath("//input[@type='submit']").click()                 XPATH METHOD
#driver.find_element_by_css_selector("input[value='Submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
#print(driver.find_element_by_css_selector("[class*='alert-success']").text)       #CSS METHOD 2ND FORMULA
print(driver.find_element_by_xpath("//*contains(@class='alert-success']").text)