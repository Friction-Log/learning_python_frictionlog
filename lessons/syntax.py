
# Print hello world
print("Hello World")

# create a string variable
my_string = "Hello World"

# concatenate two strings
print(my_string + "!!!")

# interpolate a string
print("Hello %s" % "World")

# interpolate a string with a number
print("Hello %s %d" % ("World", 42))

# interpolate a string and assign to a variable
greeting = "Hello %s" % "World"

# find the length of a string
print(len(greeting))

# find a letter in a string
print("H" in greeting)

# return the index of a letter in a string
print(greeting.index("H"))

# reverse a string
print(greeting[::-1])

# handle exceptions
try:
	print(greeting[100])
except IndexError:
	print("Index out of bounds")

# Create a variable with a list
my_list = [1, 2, 3]

# destructure a list
a, b, c = my_list

print(a, b, c)

# Add two numbers
x = 2
y = 3
print(x + y)

# Divide two numbers
x = 10
y = 3
print(x / y)

# Two numbers divided by each other
x = 10
y = 3
print(x // y)

# Two numbers divisible by each other
x = 10
y = 3
print(x % y)

# Round a number
x = 10.5
print(round(x))

# Average of a list
my_list = [1, 2, 3, 4, 5]
print(sum(my_list) / len(my_list))

# Change variable from a string to an integer
my_string = "123"
my_int = int(my_string)
print(my_int)

# Change variable from integer to a string
my_int = 123
my_string = str(my_int)
print(my_string)

# Int64
x = 1234567890123456789
print(x)

#Float64
x = 1.2345678901234567890
print(x)

# Int64 to Float64
x = 1234567890123456789
print(float(x))

# Multi line string
my_string = """
This is a multi-line string.
This is the second line.
"""
print(my_string)

# Write a boolean check
my_string = "Hello World"

# if statement 
if my_string == "Hello World":
	print("String is equal to 'Hello World'")

# if else statement
if my_string == "Hello World":
	print("String is equal to 'Hello World'")
else:
	print("String is not equal to 'Hello World'")

# if elif else statement
if my_string == "Hello World":
	print("String is equal to 'Hello World'")
elif my_string == "Hello World!!":
	print("String is equal to 'Hello World!!'")
else:
	print("String is not equal to 'Hello World'")

# check if type is a number
if type(my_string) is int:
	print("String is an integer")


