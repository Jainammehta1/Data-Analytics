import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)
sns.scatterplot(data=data,x="total_bill",y="tip",hue="smoker",palette="viridis")
plt.show()

d=pd.read_excel("ESD.xlsx")
print(d)
sns.scatterplot(data=d,x="Age",y="Annual Salary",hue="Gender")
plt.legend()
plt.show()