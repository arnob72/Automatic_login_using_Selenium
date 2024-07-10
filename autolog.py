from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from getpass import getpass 


username = input("Enter your username: ")
password = getpass("give your password: ")

service = Service("C:\\Devs\\webDriver\\geckodriver.exe")
firefox_options = Options()

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get("https://www.facebook.com/")

username_textbox = driver.find_element(By.ID, "email")
username_textbox.send_keys(username)

password_textbox = driver.find_element(By.ID, "pass")
password_textbox.send_keys(password)

login_button = driver.find_element(By.ID, "loginbutton")
login_button.click()