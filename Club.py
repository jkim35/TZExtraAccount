# Imports
import pandas as pd
import pyautogui as robot
from datetime import date,timedelta
import time
#Current date
current_date = pd.to_datetime(date.today())

#Reading the data
data=pd.read_csv("TestData.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data)

#Filtering the data
specific_date = pd.to_datetime(date.today()+timedelta(days=2))
print(data.loc[(data.Date <= specific_date)&(current_date<=data.Date),["Name","Date","Time","Type"]])
filteredData = data.loc[(data.Date <= specific_date)&(current_date<=data.Date),["Name","Date","Time","Type"]]
filteredData = filteredData.reset_index(drop=True)
filteredData = filteredData.reset_index(drop=True)
#Changing the data type
filteredData['Name'] = filteredData['Name'].astype(str)
filteredData['Type'] = filteredData['Type'].astype(str)
filteredData['Date'] = filteredData['Date'].astype(str)
filteredData['Time'] = filteredData['Time'].astype(str)
#While loop
x=0
numRows = len(filteredData)
time.sleep(4)
while(x<numRows):
    print(filteredData.iloc[x:x+1,1])
    name = filteredData.iloc[x:x+1,0].astype(str)
    dater = filteredData.iloc[x:x+1,1].astype(str)
    timed = filteredData.iloc[x:x+1,2].astype(str)
    type = filteredData.iloc[x:x+1,3].astype(str)
    print(dater)
    robot.write(name.to_string(),interval=0.05)
    robot.write(dater.to_string(),interval=0.05)
    robot.write(timed.to_string(),interval=0.05)
    robot.write(type.to_string(),interval=0.05)
    x+=1