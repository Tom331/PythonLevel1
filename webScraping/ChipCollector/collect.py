from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/Thomas/Desktop/Java/chromedriver.exe")
driver.get("http://hotmail.com")

elem = driver.find_element_by_name("loginfmt")
elem.send_keys("t.alain@live.com")

elem = driver.find_element_by_id("idSIButton9")
elem.send_keys(Keys.ENTER)


elem = driver.find_element_by_name("passwd")
wait = WebDriverWait(driver, 5)

wait.until(EC.staleness_of(elem))
elem = driver.find_element_by_name("passwd")
elem.send_keys("tga1111")

elem = driver.find_element_by_id("idSIButton9")
elem.send_keys(Keys.ENTER)


#INBOX IS NOW OPEN


elem = driver.find_element_by_css_selector("button[class*='_n_j']")
elem.click()
elem = driver.find_element_by_css_selector("input[class*='_is_x']")
elem.send_keys("myvegas")
elem.send_keys(Keys.ENTER)


#MYVEGAS EMAILS ARE NOW LOADED


emails = driver.find_elements_by_css_selector("div[class*='_lvv2_e ms-fcl-np ms-fwt-sl']")
numEmails = len(emails)
pos = 0

while(pos < numEmails):
    emails[pos].click()
    driver.execute_script("window.history.go(-1)")
    pos = pos + 1

    
#http://stackoverflow.com/questions/41926271/storing-emails-in-list-and-going-through-them-using-selenium
