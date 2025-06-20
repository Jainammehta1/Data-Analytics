import matplotlib.pyplot as plt

brands=["oneplus","Apple","Samsung","Nokia"]
x=[22,35,30,10]
c=["red","silver","gold","pink"]

plt.pie(x,labels=brands,colors=c,autopct="%.2f")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt  # use plt instead of pl by convention

# Load data from Excel
data = pd.read_excel("expense.xlsx")
df = pd.DataFrame(data)

# Group by Payment Mode
groupedby = df.groupby("Payment Mode")["Amount"].sum()
print(groupedby)


plt.pie(groupedby.values, labels=groupedby.index, autopct='%1.1f%%')
plt.title("Expenses by Payment Mode")
plt.show()

# Print original DataFrame
print(df)
