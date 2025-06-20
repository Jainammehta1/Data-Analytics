import matplotlib.pyplot as plt
x=[30,40,50,60,70,80,90,100,10,20,1,2,3,11,12,13]
plt.hist(x,bins=20,edgecolor="black",color="pink")
plt.show()

import pandas as pd
import matplotlib.pyplot as pl
data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)

pl.hist(df["Age"],bins=15)
pl.show()