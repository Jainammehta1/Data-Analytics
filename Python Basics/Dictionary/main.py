Employee={"name":"Jhon",
          "age":24,
          "gender":"male"}
print(Employee)

#To access a particular element
print(Employee["name"])

#Iteration in Dictionaries
Student={"Name":"Jainam mehta",
         "Roll number":53,
         "Gender":"Male"}

#Printing all the key names one by one
for x in Student:
    print(x)

#Printing all the value names one by one
for x in Student:
    print(Student[x])

#Using Value function
for x in Student.values():
    print(x)

#Using items function
for x,y in Student.items():
    print(x,"=",y)