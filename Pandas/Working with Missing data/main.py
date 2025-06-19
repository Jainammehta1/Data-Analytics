import pandas as pd
import numpy as np
data=pd.read_csv("People.csv")
print(data)

#Checking the Null Value
print(data.isnull().sum())

#To drop the null data completely-Not recommended
# print(data.dropna())

#To add or replace the null values
data["Job Title"]=data["Job Title"].replace(np.nan,"Scientist")
print(data) #I have changed the job title here

data["Date of birth"]=data["Date of birth"].replace(np.nan,"1992-11-12")
print(data)#The date of birth is changed
