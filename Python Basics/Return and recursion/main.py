#RETURN
def hello():
    return("Hello world")
print(hello())

def add(x,y):
    return("The addition is ",x+y)
print(add(20,25))


#RECURSION
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(5))
