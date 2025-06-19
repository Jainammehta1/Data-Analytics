import pandas as pd
data=pd.read_excel("ESD.xlsx")
print(data)

#Groupby in terms of gender and Department
a=data.groupby(["Department","Gender"]).agg({"EEID":"count"})
print(a)

#Groupby in terms of Annual maximum salary on basis of country and age
b=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max"})
print(b)