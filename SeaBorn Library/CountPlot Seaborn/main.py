#To see the count in the dataset countplot is used

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)
#To change the color u have to use pallete
sns.countplot(data=data,x="day",palette="bright")
plt.show()

df=pd.read_excel("ESD.xlsx")
print(df)
sns.countplot(data=df,x="Department",palette="pastel")
plt.xticks(rotation=40)
plt.show()