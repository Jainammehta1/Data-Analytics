import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
NOP1=[5,10,30,20,35,50,100]#Number of peoples
NOP2=[10,20,30,25,40,50,90]
NOP3=[9,10,50,60,70,90,100]
plt.stackplot(days,NOP1,NOP2,NOP3,labels=["Week1","Week2","Week3"])
plt.legend()
plt.show()

import pandas as pd
import matplotlib.pyplot as pl

# Load and prepare data
data = pd.read_excel("ESD.xlsx")
df = pd.DataFrame(data)
df2 = df.head(50)


x = df2["Age"]
y1 = df2["Annual Salary"]

# Create the stack plot
pl.stackplot(x, y1)

pl.show()
