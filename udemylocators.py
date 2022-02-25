from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("ARYAN")
driver.find_element_by_css_selector("input[name='name']").send_keys("kanti")
driver.find_element_by_name("email").send_keys("prajapati")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
#print(driver.find_element_by_css_selector("[class*='alert-success']").text)
driver.find_element_by_xpath("//*[contains(@class='alert-success']").text
#[class*='alert-success'].
#//*[contains(@class='alert-success']