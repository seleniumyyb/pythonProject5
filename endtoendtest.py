from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\Users\\kanti\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe")
#C:\\Users\\kanti\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe
#C:\Users\kanti\Downloads\geckodriver-v0.30.0-win64\\geckodriver.exe
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
products= driver.find_elements_by_xpath("//div[@class='card h-100']")
#//div[@class='card h-100']/div /h4/ a
# product=//div[@class='card h-100']/div /h4/ a
for product in products:
    productName=product.find_element_by_xpath("div/h4/a").text
    if productName=="Blackberry":
        #add into cart
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)
successText=driver.find_element_by_class_name("alert-success").text
assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")

