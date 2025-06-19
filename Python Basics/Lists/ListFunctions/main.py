#Length of a list

a=["Jai","Heyy","Onion","Heyy"]
print(len(a))

#Count- Occurence of an element
print(a.count("Heyy"))

#Add the element
a.append("SVKM")
print(a)

#Add the element in specific location
a.insert(1,"Vision")
print(a)

#Remove from list
a.remove("Vision")
print(a)

#To remove from a certain location
print(a.pop(1))
print(a)

#To create a copy pf list
b=["Hello","Heyy"]
c=b.copy()
print(c)

#To access an element
print(b.index("Hello"))

#Extend the list
d=["Thor","Spiderman"]
b.extend(d)
print(b)

#Reverse the list
b.reverse()
print(b)

#Sort the list
b.sort()
print(b)

#Clear the data from list
b.clear()
print(b)