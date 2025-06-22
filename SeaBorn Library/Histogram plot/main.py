import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
sns.histplot(data=data,x="day",hue="sex",palette="spring",kde=True)
plt.show()