import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
# print(data)

#default value is scatterplot
#KIND is used to change the plot
sns.relplot(data=data,x="tip",y="total_bill",hue="sex",kind="line")
plt.show()