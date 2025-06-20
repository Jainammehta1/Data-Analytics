import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[45,35,44,77,33]
plt.subplot(1,2,1)
plt.title("Age")
plt.plot(x,y)


x=[5,6,7,8]
y=[67,50,56,82]
plt.subplot(1,2,2) #row,column
plt.title("Weight")
plt.bar(x,y)
plt.suptitle("Employee Data")
plt.show()