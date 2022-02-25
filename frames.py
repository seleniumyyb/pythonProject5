from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#iframe, frameset, frame
#frame id and frame name  or index value

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()

driver.find_element_by_css_selector("#tinymce").send_keys("i m able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)