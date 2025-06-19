import numpy as np

#Append-Adds the element in the last

arr=np.array([1,2,3,4])
print("The array after appending is ",np.append(arr,5))

#Insert
print("The array after inserting is ",np.insert(arr,2,9))

#Delete
print("The array after deleting is ",np.delete(arr,[2]))