#for loop

for i in range(1,6):
    print(i)

#Multiplication table
n=7
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#while loop

a=1
while a<=5:
    print(a)
    a=a+1

#Nested loop
print("Nested loop")
for i in range(1,4):
    for j in range(1,11):
        print(j,end="")
    print()