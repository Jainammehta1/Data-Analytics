import pandas as pd

data={"Emp Id":["E01","E02","E03","E04","E05","E06"],
      "Names":["Ram","shyam","jai","veeru","joka","hari"],
      "Age":[12,13,14,15,16,17]}

data2={"Emp Id":["E01","E02","E03","E04","E05","E06"],
       "Salary":[45000,55000,6000,8080,90909,10000]}

df1=pd.DataFrame(data)
print(df1)
print()
df2=pd.DataFrame(data2)
print(df2)

#Merge
print(pd.merge(df1,df2,on="Emp Id"))

#Left Merge
print(pd.merge(df1,df2,on="Emp Id",how="left"))

#Right Merge
print(pd.merge(df1,df2,on="Emp Id",how="right"))
print()

#Concatenate
data1={"Emp Id":["E01","E02","E03","E04","E05","E06"],
      "Names":["Ram","shyam","jai","veeru","joka","hari"],
      "Age":[12,13,14,15,16,17]}
data3={"Emp Id":["E07","E08","E09","E10","E11","E12"],
      "Names":["Ram","shyam","jai","veeru","joka","hari"],
      "Age":[20,21,22,25,26,27]}
df=pd.DataFrame(data1)
print(df)
print()
d2=pd.DataFrame(data3)
print(d2)
print(pd.concat([df,d2]))