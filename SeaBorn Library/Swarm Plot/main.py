import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")

#Strip and swarm are indirectly same
#Dodge is used to seperate the values
sns.swarmplot(data=data,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()