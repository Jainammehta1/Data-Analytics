#Write a program to display persons name age address

name="Jainam"
age=21
address="Mumbai"
print(name)
print(age)
print(address)

#Swapping two variables

x=12
y=13
temp=x
print(temp)
x=y
print(x)
y=temp
print(y)
print("Value of x is",x)
print("Value of y is",y)

#Method 2
a=10
b=30
a,b=b,a
print(a)
print(b)

#Write a program to check number is positive or not
num=int(input("Enter the number: "))
if num>0:
    print("Number is positive")
else:
    print("The number is negative")

#Write a program to check the number is even or odd
number=int(input("Enter the number here to check even or odd : "))
if number%2==0:
    print("It is even number")
else:
    print("It is an odd number")

#Write a program to create area calculator

print("*****AREA CALCULATOR*****")
print("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of cricle
press 5 to get area of triangle""")
choice=int(input("Enter a number between 1-4 "))
if choice==1:
    side=float(input("Enter the length of one side"))
    area=side**2
    print("The area of square is:",area)
elif choice==2:
    length=float(input("Enter the length"))
    width=float(input("Enter the width"))
    area=length*width
    print("The area of rectangle is:", area)
elif choice==3:
    radius=float(input("Enter the radius of circle"))
    area=((22/7)*(radius**2))
    print("The area of cricle is",area)
elif choice==4:
    base=float(input("Enter the base"))
    height = float(input("Enter the height"))
    area =0.5*base*height
    print("The area of triangle is", area)

#Fibonacci Series
a=0
b=1
print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)

#Prime number
num=int(input("Enter the number"))
if num<=1:
    print("It is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Number is not a prime number")
            break
    else:
        print("It is prime number")

