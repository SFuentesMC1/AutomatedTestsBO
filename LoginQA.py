from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


options = Options()
options.binary_location = "C:\\DRIVERS\\chrome-win64\\chrome.exe"
service = Service("C:\\DRIVERS\\chromedriver-win64\\chromedriver.exe")

d = webdriver.Chrome(service=service, options=options)
d.get("https://login.qa-ire-labs.dev/es")

d.maximize_window()
time.sleep(3)

menuLogin = d.find_element(By.XPATH, "(//a[contains(@class,'btn r-12')])[2]")
menuLogin.click()
time.sleep(2)

usr = d.find_element(By.XPATH,"(//input[@name='email'])[1]").send_keys("Sergio")
time.sleep(2)

psw = d.find_element(By.XPATH,"(//input[contains(@class,'form-control email')])[2]").send_keys("passwordTest")
time.sleep(2)

btnLogin = d.find_element(By.XPATH, "(//button[contains(@class,'btn btn--white')])[1]")
btnLogin.click()
time.sleep(2)

usrclear = d.find_element(By.XPATH,"(//input[@name='email'])[1]").clear()
time.sleep(2)
usrcorrect = d.find_element(By.XPATH,"(//input[@name='email'])[1]").send_keys("sergio.fuentes+pruebas_qa@mc1global.com")
time.sleep(2)
btnLogin.click()

time.sleep(7)
d.close() 