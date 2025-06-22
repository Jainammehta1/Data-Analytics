import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
a=sns.FacetGrid(data,col="day")

#By using map u can create multiple plot
a.map(sns.barplot,x="day",y="tip",data=data)
plt.show()