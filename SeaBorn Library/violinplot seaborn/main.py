import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
sns.violinplot(data=data,x="total_bill")
plt.show()

df=pd.read_excel("ESD.xlsx")
sns.violinplot(data=df,x="Bonus %")
plt.show()