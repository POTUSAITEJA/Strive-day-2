import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



'''
The day of the week (Tuesday)
The date (01/06/2020)
A short description of the conditions (Clear early then increasing cloudiness after midnight. Low 41F. Winds light and variable)
The temperature low and high, with a function of your own to convert into Celsius
For each element you scrape, The name of the item you targetted (ex: DailyContent--daypartDate--3MM0J)
'''

df = pd.DataFrame(columns=["Item_name","weekday","date","Description","Temperature °C"])

url = 'https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c'
path = r'C:/Users/User/Downloads/chromedriver_win32'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[3]/button[1]').click()

# sleep(5)

# '''
# target = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[4]/summary')
# actions = ActionChains(driver)
# actions.move_to_element(target)
# actions.perform()
# sleep(2)
# #button = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[2]/summary')
# #for button in buttons:
# target.click()
# '''

# rows = driver.find_elements_by_xpath('//div[@data-testid="DailyContent"]')



# weekday = []
# Item_name = []
# date_list = []
# description = []
# Temperature_initial = []
# Temperature = []

# for i in rows:
#     data = i.text.split('\n')
#     description.append(data[-1])
#     print(description)


# df2 = pd.DataFrame(list(zip(Item_name, weekday, date_list, description, Temperature)), columns=df.columns)
# df = df.append(df2, ignore_index=True)
