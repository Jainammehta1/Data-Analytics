import numpy as np

a=[[10,20,30,40,50],[60,70,80,90,25]]
arr=np.array(a)
print(arr)

#Shape Function
print(arr.shape)

#Length
print(len(arr)) #Gives the number of arrays created

#Size
print(arr.size) #Number of elements

#Data type
print(arr.dtype)

#Converting the type
print(arr.astype(float))