from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ffox = webdriver.Firefox()

def connect_to_browser():

   ffox.get('https://presenzeonline.manpower.it/Site/Login.aspx?ReturnUrl=%2fsite%2fdefault.aspx')
   time.sleep(5)
   cookies = ffox.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
   cookies.click()
  
def fill_login_fields():

   user = ffox.find_element(by=By.XPATH, value='//*[@id="txtUser"]')
   user.send_keys('')
   
   password = ffox.find_element(by=By.XPATH, value='//*[@id="txtPassword"]')
   password.send_keys('')
   
   login = ffox.find_element(by=By.XPATH, value='//*[@id="btnLogin"]')
   login.click()
   
def fill_manp_fields():

   buttonVis = ffox.find_element(by=By.XPATH, value='//*[@id="ctl00_ContentTop_btnVisualizza"]')
   buttonVis.click()
   
connect_to_browser()
fill_login_fields()
fill_manp_fields()

