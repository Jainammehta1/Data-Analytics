import pandas as pd
df=pd.read_excel("ESD.xlsx")
print(df)
df.loc[(df["Bonus %"]==0),"GetBonus"]="No bonus"
df.loc[(df["Bonus %"]>0),"GetBonus"]=" bonus"
print(df.head(10))#Here we are checking whether the employess have got bonus or not

data=pd.read_csv("People.csv")
print(data)
data["Full Name"]=data["First Name"].str.capitalize()+" "+data["Last Name"]
print(data) #The first name and last is being concatenated

