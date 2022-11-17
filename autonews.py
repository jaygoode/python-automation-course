from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.oldschool.runescape.com/'
path = '/Users/johnny/Downloads/chromedriver_win32/chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
input()
