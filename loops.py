#Loops
-While Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1 
while x < 7:
	print(x)
	x += 1


while loop requires variable ready

x = 1
while x < 7:
	print (x)
	if x == 5:
		break
	x += 1



For Loops

# for loops is iterating over a sequence

fruits = ['apple', 'banana', 'orange', 'pineapple', 'coconut', 'coconut', 'cucumber']
for x in fruits:
	print(x)


# Loopings in string

for x in 'pineapple':
	print(x)


# the break statement

# stop after condition


fruits = ['apple', 'banana', 'orange', 'pineapple', 'coconut', 'coconut', 'cucumber']
for x in fruits:
	print(x)
	if x == 'pineapple':
		break

# the continue statement - stop the current iteration
fruits = ['apple', 'banana', 'orange', 'pineapple', 'coconut', 'coconut', 'cucumber']
for x in fruits:
	if x == 'orange':
		continue
	print(x)

#stop before condition
fruits = ['apple', 'banana', 'orange', 'pineapple', 'coconut', 'coconut', 'cucumber']

for x in fruits:
	print(x)
	if x == 'coconut':
		break
		print(x)


# The range () function - a set of code a specified number of times

for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)


for x in range(10, 100, 5):
	print(x)


#Nested Loops

NumberA = [1, 2, 3, 4, 5]
NumberB = [1, 2, 3, 4, 5]
NumberC = [1, 2, 3, 4, 5]

for x in NumberA:
	for y in NumberB:
		for z in NumberC:
			print(x, y, z) 


words = ['cat', 'window', 'defenstrate', 'hello world']
for w in words:
		print(w, len(w))


------------

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		#loop fell through without finding a factor
		print(n, 'is a prime number')


for num in range(2, 10):
	if num %  2 == 0:
		print("found an even number")
		pass
	print('found a number', num)