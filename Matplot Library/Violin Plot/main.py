import matplotlib.pyplot as plt
x=[30,40,50,60,70,80,90,100,10,20,1,2,3,11,12,13,60,77,88,99]
plt.violinplot(x,showmedians=True)
plt.show()

import pandas as pd
import matplotlib.pyplot as pl
data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
pl.violinplot(df["Annual Salary"],showmedians=True)
pl.show()
