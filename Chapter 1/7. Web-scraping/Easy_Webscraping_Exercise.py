from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import timedelta

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
df = pd.DataFrame(columns=["Item_name","weekday","date","Description","Temperature °C"])


page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YVLOoLgzaUk')

soup = BeautifulSoup(page.content, 'html.parser')


div = soup.find_all('div',id="current_conditions_detail")[0]
td = div.find_all("td")

date ="".join(td[-1].text.strip().split()[:2])
date = date.replace("Sep","-9-")+"2021"
date = datetime.strptime(date,'%d-%m-%Y').date()

Temperature = td[-5].text.split()[-1].replace("(","").replace(")","")

Item_name = "current_conditions_detail"
weekday = week_days[date.weekday()]

df2 = pd.Series([Item_name, weekday, date, None, Temperature], index=df.columns)
df = df.append(df2, ignore_index=True)

#Extract next 9 periods
div = soup.find_all('div',class_="tombstone-container")
weekday = []
Item_name = []
date_list = []
description = []
Temperature_initial = []
Temperature = []
for i in div:
    Item_name.append("tombstone-container")
    weekday.append(i.find("p", class_="period-name").text)
    date += timedelta(days=1)
    date_list.append(date)
    try:
        Temperature_initial.append(i.find("p", class_="temp temp-low").text)
    except:
        Temperature_initial.append(i.find("p", class_="temp temp-high").text)

for j in Temperature_initial:
    Temperature.append(str(int((int(j.split()[1])-32)*0.5556))+"ºC")

div_description = soup.find_all('div',class_="col-sm-10 forecast-text")
description = []
for el in div_description:
    description.append(el.text)

df2 = pd.DataFrame(list(zip(Item_name, weekday, date_list, description, Temperature)), columns=df.columns)
df = df.append(df2, ignore_index=True)
print(df)