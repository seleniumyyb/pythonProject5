from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="C:\\Users\\kanti\\Downloads\\firefoxgecko64\\geckodriver.exe")
#C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe
#C:\Users\kanti\Downloads\geckodriver-v0.30.0-win64.zip
#C:\Users\kanti\Downloads\firefoxgecko64
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action= ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()     #right click function
action.double_click(driver.find_element_by_id("double-click")).perform()
alert=driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me"== alert.text
alert.accept()

print(driver.find_element_by_id("displayed-text").is_displayed)
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed)