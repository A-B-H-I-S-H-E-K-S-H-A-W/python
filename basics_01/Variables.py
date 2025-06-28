#1 Basic Variable ------------

"""
Types of variable

int
float
bool
string
None
"""
x = 4 # This is of type int
y = "String" # This is of typr string 
y = 5
# print(x + y) TypeError
print(x)
print(y)

print(type(x)) # Prints the type 
# <class 'int'>



#2 Variable Names ----------

# Short names 

x = 5
y = "Hello"
z = False

print(x, y, z)

# Descriptive Names

price = 50
name = "Abhi"
isLoggedIn = False

print(price, name, isLoggedIn)


"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#3 Assign multi values

x, y, z = "Orange", "Banana", "Cherry" #Assign multiple values 
print(x)
print(y)
print(z)

x = y = z = "Cherry" # Assign single value to multiple variables
print(x)
print(y)
print(z)

fruits = ["Cherry", "Apple", "Mango"]

x, y, z = fruits # Unpack a collection
print(x)
print(y)
print(z)

#3 Output Variables

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)