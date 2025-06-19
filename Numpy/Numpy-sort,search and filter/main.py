import numpy as np

#Sorting array in ascending array
a=np.array([3,2,5,6,1])
print(np.sort(a))

#Search
b=np.where(a==3)
print(b)
print(np.searchsorted(a,3)) #Index of the value will be given

#Filter
arr=np.array([10,20,30])
fil=[True,False,True]
new=arr[fil]
print(new)