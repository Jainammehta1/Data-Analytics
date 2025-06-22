import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#In built datasets are presents in seaborn
data=sns.load_dataset("tips")
print(data)
sns.barplot(data=data,x="day",y="tip",hue="sex",palette="viridis")
plt.plot()
plt.show()