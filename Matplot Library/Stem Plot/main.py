import matplotlib.pyplot as plt
x=[30,40,50,60,70,80,90,100,10,20,1,2,3,11,12,13,60,77,88,99]
plt.stem(x,)
plt.show()

import pandas as pd
import matplotlib.pyplot as pl
data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
df2=(df.head(50))
print(df)
pl.stem(df2["Age"])
pl.show()