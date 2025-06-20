import matplotlib.pyplot as plt

x=["Day1","Day2","Day3","Day4","Day5"]
y=[300,429,250,230,400]
y1=[500,450,300,250,100]
plt.plot(x,y,marker="o",ls="--",color="red",label="week1") #LS stands for linestyle
plt.plot(x,y1,marker="o",ls="--",color="green",label="week2")
plt.legend() #It denotes which point represents anything
plt.show()

import pandas as pd
import matplotlib.pyplot as pl  # <- imported as 'pl'

data = pd.read_excel("expense.xlsx")
df = pd.DataFrame(data)

groupedby = df.groupby("Category")["Amount"].sum()
print(groupedby)

# Plotting with correct alias
pl.plot(groupedby.index.tolist(),groupedby.values)
pl.show()

print(df)



