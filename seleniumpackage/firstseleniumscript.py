from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
print(type(driver))
driver.get("http://www.google.com")
mypageTitle=driver.title
print(mypageTitle)
print(driver.quit)
driver.quit()

#"C:\\Users\\kanti\\Downloads\\chromedriver_win32.exe
#Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe
