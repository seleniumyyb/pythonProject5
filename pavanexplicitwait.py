from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")
