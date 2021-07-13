from math import sqrt

# function with int parameter
def my_function(a: str):
	print(a)

my_function(3)

# function with type annotation
def my_function2(a: str) -> str:
	return a

print(my_function2(3))

# import sqrt from math and use it
print(sqrt(9.4323))

# import alias from math
# from math import sqrt as square_root

# function with list parameter
def my_function3(a: list):
	for i in a:
		print(i)

my_function3([1, 2, 3, 4, 5])

# function with dictionary parameter
def my_function4(a: dict):
	for key, value in a.items():
		print(key, value)

my_function4({'a': 1, 'b': 2, 'c': 3})

# function with tuple parameter
def my_function5(a: tuple):
	for i in a:
		print(i)

my_function5(('a', 'b', 'c', 'd'))

# function with set parameter
def my_function6(a: set):
	for i in a:
		print(i)

my_function6({'a', 'b', 'c', 'd'})

# function with function parameter
def my_function7(a: callable):
	a()

# make an http request async
async def my_function8(a: callable):
	a()

# my_function8(lambda: print('hello'))

