# Imports
import pandas as pd
import pyautogui as robot
from datetime import date
#Current date + Formatter
current_date = date.today()

print("Formatted Date:", current_date)
#Reading the data
data=pd.read_csv("TestData.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data)

#Filtering the data
print(data.loc[(data.Date == current_date),["Name","Date","Time"]])