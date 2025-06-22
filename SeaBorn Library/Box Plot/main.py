import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)

sns.boxplot(data=data,x="tip",y="sex",palette="bright")
plt.show()