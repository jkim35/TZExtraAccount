# Imports
import pandas as pd
import pyautogui as robot
from datetime import date,timedelta
import time
#Current date
current_date = pd.to_datetime(date.today())

#Reading the data
data=pd.read_csv("DataClubs - Form Responses 1.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data)

#Filtering the data
specific_date = pd.to_datetime(date.today()+timedelta(days=7))
print(data.loc[(data.Date <= specific_date)&(current_date<=data.Date),["Name","Date","Time","Type","Location"]])
filteredData = data.loc[(data.Date <= specific_date)&(current_date<=data.Date),["Name","Date","Time","Type","Location"]]
filteredData = filteredData.reset_index(drop=True)
filteredData = filteredData.reset_index(drop=True)
#Changing the data type
filteredData['Name'] = filteredData['Name'].astype(str)
filteredData['Type'] = filteredData['Type'].astype(str)
filteredData['Date'] = filteredData['Date'].astype(str)
filteredData['Time'] = filteredData['Time'].astype(str)
filteredData['Location'] = filteredData['Location'].astype(str)
#While loop
x=0
numRows = len(filteredData)
time.sleep(1)
current_date = current_date.strftime("%m/%d/%Y")
specific_date = specific_date.strftime("%m/%d/%Y")
robot.write("t")
robot.write(current_date,interval=0.05)
robot.write("---",interval=0.05)
robot.write(specific_date,interval=0.05)
robot.leftClick(500,600)
while(x<numRows):
    print(filteredData.iloc[x:x+1,1])
    name = filteredData.iloc[x:x+1,0].astype(str)
  #  name = name[1:]
    dater = filteredData.iloc[x:x+1,1].astype(str)
   # dater = dater[1:]
    timed = filteredData.iloc[x:x+1,2].astype(str)
 #   timed = timed[1:]
    type = filteredData.iloc[x:x+1,3].astype(str)
    loc = filteredData.iloc[x:x+1,4].astype(str)
   # type = type[1:]
    print(dater)
    robot.write("t",interval=0.05)
    robot.write(name.to_string()[5:],interval=0.05)
    robot.write("//",interval=0.05)
    robot.write(dater.to_string()[10:],interval=0.05)
    robot.write("//",interval=0.05)
    robot.write(timed.to_string()[5:],interval=0.05)
    robot.write("//",interval=0.05)
    robot.write(type.to_string()[5:],interval=0.05)
    robot.write("//",interval=0.05)
    robot.write(loc.to_string()[5:],interval=0.05)
    x+=1
    robot.leftClick(500,600)
