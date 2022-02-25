from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
#driver= webdriver.Chrome(executable_path="C:\\Users\\kanti\\Downloads\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\kanti\\AppData\\Local\\Temp\\Temp1_geckodriver-v0.30.0-win32.zip\\geckodriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()