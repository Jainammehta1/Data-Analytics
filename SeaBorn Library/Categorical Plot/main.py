import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)

#Bydefault it is strip plot and in order to change the plot "kind" is used
sns.catplot(x="day",y="tip",data=data,hue="sex",kind="violin")
plt.show()