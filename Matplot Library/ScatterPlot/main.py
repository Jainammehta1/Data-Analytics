import matplotlib.pyplot as plt
import numpy as np

x=np.random.randint(1,10,50,)
y=np.random.randint(10,100,50)
color=np.random.randint(10,100,50)
plt.scatter(x,y,marker="*",cmap="hot",c=color)
plt.colorbar()
plt.show()

import pandas as pd
import matplotlib.pyplot as pl
import numpy as n

data=pd.read_excel("ESD.xlsx")
df=pd.DataFrame(data)
print(df)
plt.scatter(df["Age"],df["EEID"],)
plt.show()