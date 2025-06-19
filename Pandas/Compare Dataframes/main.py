import pandas as pd
dic={"Fruits":["Mangoes","Banana","Grapes","papaya"],
     "Price":[100,15,20,25],
     "Quantity":[15,10,10,3]}
df=pd.DataFrame(dic)
print(df)
print()

#CREATING SAME DATAFRAME WITH DIFFERENT VALUES
df2=df.copy()
df2.loc[0,"Price"]=120
df2.loc[1,"Price"]=175
df2.loc[3,"Price"]=30
df2.loc[0,"Quantity"]=12
df2.loc[1,"Quantity"]=15
df2.loc[3,"Quantity"]=5

print(df2)
print()

#COMPARING THE DATAFRAMES
print(df.compare(df2))