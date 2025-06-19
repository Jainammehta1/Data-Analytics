Student={"Name":"Jainam mehta",
         "Roll number":53,
         "Gender":"Male"}

#Get
x=Student.get("Name")
print(x)

#item
a=Student.items()
print(a)

#Keys
b=Student.keys()
print(b)

#Values
c=Student.values()
print(c)

#copy
d=Student.copy()
print(d)

#setdefault
x=Student.setdefault("Roll number",53)
print(x)