from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

user_name = "thongdoan1208@gmail.com"
password = "Thong@12082001"
driver = webdriver.Chrome('D:\Documents\Ty\Thưc tập - THE BIM FACTORY 4.7.2022\Code\chromedriver.exe')
driver.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com")
element = driver.find_element(By.ID , "modalusername")
element.send_keys(user_name)
sleep(2)
element = driver.find_element(By.ID ,"current-password")
element.send_keys(password)
sleep(2)
element.send_keys(Keys.RETURN)


wait = WebDriverWait( driver, 5 )
page_title = driver.title
assert page_title == "W3school"

element.close()