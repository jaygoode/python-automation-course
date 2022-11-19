from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime("%m%d%y")

website = 'https://www.oldschool.runescape.com/'
path = '/Users/johnny/Downloads/chromedriver_win32/chromedriver'

options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="news-article__details"]')

links = []

for container in containers:

    link = container.find_element(
        by="xpath", value='./p/a').get_attribute("href")

    links.append(link)


my_dict = {'links': links}

df_headlines = pd.DataFrame(my_dict)

final_path = os.path.join(application_path, f'headlines-{month_day_year}.csv')
df_headlines.to_csv(final_path)

driver.quit()
