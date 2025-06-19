import numpy as np

#Creating a Array-------

#Single Dimensional Array
arr=np.array([10,20,30,40,50])
print(arr)

#Slicing
print(arr[0:3])
print(arr[3:])
print(arr[:3])


#Multidimensional Array
arr1=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(arr1)

#Slicing
print(arr1[0:2,0:2])
print(arr1[0,1:3])#0 indicates the first row
print(np.shape(arr1)) #Shows the number of rows and columns
print(np.size(arr1))  #Shows the size of array
print(np.ndim(arr1))  #Shows the dimensions



