import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[45,32,78,99,85]
z=[32,42,55,67,72]
plt.figure(figsize=[5,3]) #Adjust the size of the plot
plt.plot(x,y,label="male")
plt.plot(x,z,label="female")

#TO CHANGE THE LOCATION OF THE LEGEND
#0-Bottom left bydefault
#1-Top Right
#2-Top Left
#3-Bottom Left
#4-Bottom Right
#10-Center
plt.legend(loc=1)

plt.show()