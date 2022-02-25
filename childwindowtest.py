from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
#driver.find_element_by_tag_na
childwindow = driver.window_handles[1]
#("parentid","childid")
driver.switch_to.window("childwindow")

print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.window("driver.window_handles[0]")
print(driver.find_element_by_tag_name("h3").text)