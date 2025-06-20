
import matplotlib.pyplot as plt

#Creating barplot on basis of created data
y=[98,67,88,95,88]
x=["Part1","Part2","Part3","Part4","Part5"]
color=["red","blue","green","yellow","orange"]
plt.bar(x,y,color=color)
plt.xlabel("Parts of Harry potter",fontsize=17)
plt.ylabel("Popularity",fontsize=17)
plt.title("Popularity of diffrerent parts of harry potter",fontsize=17)
plt.show()


import pandas as pd
import matplotlib.pyplot as pl

data = pd.read_excel("expense.xlsx")
df = pd.DataFrame(data)
print(df)

# Convert Payment Mode to string
df["Payment Mode"] = df["Payment Mode"].astype(str)
groupedby=df.groupby("Payment Mode")["Amount"].sum()
print(groupedby)
pl.bar(groupedby.index, groupedby.values)
pl.show()

