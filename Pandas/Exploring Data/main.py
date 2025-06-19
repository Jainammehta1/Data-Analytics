import pandas as pd
data=pd.read_csv("Sample.csv")
print(data)

#Shows data from above in the given range
print(data.head(10)) #DEFAULT VALUE IS 5

#Shows data from below in the given range
print(data.tail(10))

#To get the info/datatype of the data
print(data.info())

#Describe data-std,variance,count etc
print(data.describe())

#To check how many data is null
print(data.isnull().sum()) #.sum will count the values column vise

