import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={"Days":[1,2,3,4,5],
      "NOP":[50,33,65,23,11]}
df=pd.DataFrame(data)
print(df)
sns.lineplot(data=data,x="Days",y="NOP")
plt.show()

#Creating a plot by reading excel file
d=pd.read_excel("ESD.xlsx")
print(d)
sns.lineplot(data=d,x="Business Unit",y="Age",hue="Gender")
plt.show()
print(d)