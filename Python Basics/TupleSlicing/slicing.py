a=("Oneplus","Realme","Redmi","Nokia","Vivo")
print(a[0:2])
print(a[::2])#Gapvalue
print(a[::-1])#Reverse

#Iteration

#With for loop
for i in a:
    print(i)

#For loop with range and length in for loop
for i in range(len(a)):
    print(a[i])

# Along with while loop
i=0
while i<len(a):
    print(a[i])
    i+=1
