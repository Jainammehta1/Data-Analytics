import matplotlib.pyplot as plt
l=[10,20,30,40,50,60,70,80,90,100]
plt.boxplot(l)
plt.show()

import pandas as pd
import matplotlib.pyplot as pl

# Load data from Excel
data = pd.read_excel("expense.xlsx")
df=pd.DataFrame(data)
print(df)
print(df.columns)
pl.boxplot(df["Amount"])
pl.show()