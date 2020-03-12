#fibonacci.py

#Fibonacci numbers module

#n = int(input('Please enter a number: '))

# def - function


def fib(n):
	a, b = 0, 1
	while  a<n:
		print(a, end = ' ')
		a, b = b, a+b
	print()


#Go to Fibonacci Powerpoint

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result