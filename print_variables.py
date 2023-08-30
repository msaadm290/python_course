x = 5
y = "John"
print(x)
print(y)

#variable types

print(type(x))
print(type(y))

#type casting 

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Many Assign Values to Multiple Variables

x, y, z = "Banana", "orange", "cherry"
print(x)
print(y)
print(z)

#global variables

x = "awesome"

def myfunc():
    print("python is " + x)


myfunc()   

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()


print("Python is " + x)
