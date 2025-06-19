import numpy as n

#Concatenate

arr1=n.array([1,2,3])
arr2=n.array([4,5,6])
print(n.concatenate([arr1,arr2]))

#Splitting arrays

a=n.array([1,2,3,4,5,6,7])
print(n.array_split(a,2))