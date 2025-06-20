import matplotlib.pyplot as plt
x=["day1","day2","day3","day4"]
y=[30,45,25,80]
plt.step(x,y)
plt.show()

import pandas as pd
import matplotlib.pyplot as pl

# Load data
data = pd.read_excel("expense.xlsx")
df = pd.DataFrame(data)

# Group and sum amounts by category
group = df.groupby("Category")["Amount"].sum()

# Convert category names to numeric positions
x = range(len(group))  # e.g., 0, 1, 2, ...
y = group.values

# Step plot with numeric x and proper labels
pl.step(x, y, where='mid')  # 'where' controls the step position
pl.xticks(ticks=x, labels=group.index, rotation=45)  # Set category labels

pl.xlabel("Category")
pl.ylabel("Total Amount")
pl.title("Step Plot of Expenses by Category")
pl.tight_layout()
pl.show()
