import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=sns.load_dataset("exercise")
sns.barplot(data=data,x="time",y="pulse")
sns.set_style(style="ticks")
plt.show()


sns.palplot(sns.color_palette("spring"))
plt.show()