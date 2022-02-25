from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\AppData\\Local\\Temp\\Temp1_chromedriver_win32 (3).zip\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\kanti\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# create class of actionchain object
action= ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
childMenu=driver.find_element_by_link_text("Top")
action.move_to_element(childMenu).click().perform()