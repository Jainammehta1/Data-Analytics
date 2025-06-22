import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data means there is an in built dataset in this library
data=sns.load_dataset("tips")
print(data)
gp=data.groupby("day").agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()

d=pd.read_excel("ESD.xlsx")
g=d.groupby("Job Title").agg({"Annual Salary":"mean"})
sns.heatmap(g)
plt.show()