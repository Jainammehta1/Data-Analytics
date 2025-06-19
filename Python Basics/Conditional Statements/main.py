#Conditional Statement
# if,if-else,if-elif-else,Nested,short hand if

#if statement
marks=87
if marks>=90:
    print("You Have got good marks")
print("You have got average marks")

#if-else statement
a=90
if a>=90:
    print("A grade")
else:
    print("B grade")

#if-elif-else statement
mark=87
if marks>90:
    print("A grade")
elif marks>80 and marks<90:
    print("B grade")
else:
    print("PASS")

#Nested if statement
mar=99
if mar>=80:
    print("You will get a new phone")
    if mar>=95:
        print("You can also get a new bike")
else:
    print("No phone")

#Short hand if statement-One line statement
b=30
if b>=20:print("Very good") #oneline
