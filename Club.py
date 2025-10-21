# Imports
import pandas as pd
import pyautogui as robot
from datetime import date,timedelta
#Current date
current_date = pd.to_datetime(date.today())

#Reading the data
data=pd.read_csv("TestData.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data)

#Filtering the data
specific_date = pd.to_datetime(date.today()+timedelta(days=2))
print(data.loc[(data.Date <= specific_date)&(current_date<=data.Date),["Name","Date","Time","Type"]])
