from selenium import webdriver
from selenium.webdriver.support.select import Select
validateText = "option3"
driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert=driver.switch_to.alert
alertText=alert.text
assert validateText in alertText
alert.accept()
#alert.dismiss()