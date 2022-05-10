from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\Matthew\\Desktop\\Git+automation\\Automation-10\\chromedriver.exe')
driver.maximize_window()


driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('Cancle Order')
driver.find_element(By.ID, 'helpsearch').send_keys(Keys.ENTER)


