#Local Variables

x=24
print("First variable x ",x)
def hello():
    x=25
    return x
print(hello())

#Global Variable

y=24
print("First variable x ",y)
def hell():
    global y #Declared as global variable
    y=25
    return y
print(hell())
print(y)