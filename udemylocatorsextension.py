from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("kanti")
driver.find_element_by_css_selector(".password").send_keys("prajapati")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//a[text()= 'Cancel']").click()
driver.find_element_by_xpath("//*[@id='forgotPassForm']/div[1]/input[3]").click()
#//tagname[contains(text(), ‘actual-text’)]
#//tagname[text()='xxx']
#driver.find_element_by_xpath("//button[text()='Cancel']").click()
#driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/div[1]/input[3]").click()
#print(driver.find_element_by_xpath("//form[@name='login]/div[1]'/label").text)
#print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
#//div[@id='usernamegroup']/label # xpath triverse parentchild

#//form[@name='login']/div[1]/label - grandparent x path
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)