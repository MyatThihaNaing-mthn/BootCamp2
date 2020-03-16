def sayHello():
	print('Hello World')

sayHello()

#function parameter

def print_max(a, b):
	if a > b:
		print(a, 'is maximum')

	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, 'is maximum')

print_max(x, y)

x = 8
y = 11

print_max(x, y)

#Local variable

def func(x):
	print('x is', x)
	x = 2
	print('Changed Local x to ', x)
x = 50
func(x)
print('x is still', x)

x = 30

def func(x):
	x = 2

def funx(x):
	x = 10


func(x)
funx(x)

x 

func(x) + funx(x)

#Global statement

def func():
	global x

	print('x is ', x)

	x =2

	print('change global x to ', x)


# Default argument values in function

def say(message, times = 1):
	print(message*dtimes)

say('Hello')
say('World', 5)
say('Good Bye')

#keyword arguments

def func(a, b = 5, c = 10):
	print('a is', a, 'and b is', b,'and c is', c)

func(3, 8)
func(24, c = 26)
func(c = 29, a = 39)

# VarArgs parameters
# function_VarArgs.py

def total(a = 5, *numbers, **phonebook):
	print('a', a)

	for single_item in numbers:
		print('single_item', single_item)

	for first_part, second_part in phonebook.items():
		print(first_part, second_part)

total(10, 1, 2, 3, Jack = 2231, Inge =1459)

# docstring documentation string
def print_max(x, y):
	''' print the maximum of two numbers 
		the two values of ....
	'''

	x = int(x)
	y = int(y)

	if x > y:
		print('x is maximum')
	elif x < y:
		print('y is maximum')
	else:
		print('x is equal to y')

print_max(5, 9)

print(print_max.__doc__)



def paper():
	'''Another productive way to use this tool to begin
	 a daily writing routine. One way is to generate a 
	 random paragraph with the intention to try to
	 rewrite it while still keeping the original meaning.
	 The purpose here is to just get the writing started
	 so that when the writer goes onto their day's writing 
	 projects, words are already flowing from their fingers.
	'''

	print(paper.__doc__)