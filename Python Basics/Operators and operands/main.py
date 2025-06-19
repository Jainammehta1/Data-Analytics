#Arithmmetic Operators +,-,/,*,%
from operator import is_not

a=40
b=30
print("Addition is",a+b)
print("Subraction is",a-b)
print("Multiplication is",a*b)
print("Division is",a//b) #Floor division before decimal value
print("Modulus operator",a%b)

#Comparision Operators <,>,<=,>=,==,!=

print(3>2) #Greater
print(3==3) #Equalto
print(3>=3) #Greater qual
print(10!=2) #NotEqual

#Logical Operators and,or,not

print(3<4 or 3>10)
print(3>4 and 3<6)
print(not(3>2 and 3<5))

#Assignment Operators =,+=,-=,*=,/=,%=

x=50
print("This is equalsto",x)

x+=20
print(x)

x-=20
print(x)

#Identity operator is,isnot

f=1234
e=1234
print(f is e)
print(f is not e)

#Membership operator in,not in
z="Hello"
print("H" in z)
print("e" not in z) #False as it is present





