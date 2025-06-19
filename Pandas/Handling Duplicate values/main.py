import pandas as pd
data=pd.read_csv("Sample.csv")
print(data)

#Duplicate values will be shown
print(data.duplicated("Game Number").sum())

#To drop the duplicate value
print(data.drop_duplicates("Game Number"))