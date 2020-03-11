#If Else statements
If_Else_Statement.py

#Boolean Expressio

print( 20> 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals						->  x == y
Not Equals					->  x != y
Less than 					->  x < y
Less than or eqal to		->  x <= y
Greater than				->  x > y
Greater than or eqal to		->	x >= y
Boolean OR 					->  x or y, x | y
Boolean AND 				->  x and y, x & y
Boolean NOT 				->  not x


#If statement 

x = 70
y = 60

if x > y:
	print('x is greater than y')

#if ELif

x = 70
y = 60

if x > y:
	print('x is greater than y')
elif x == y:
	print('x and y are equal')
else:
	print('x is Less than y')


#	if - else-

x = 70
y = 70
if x == 0:
	print('x is zero')
elif x != 0:
	print('x is equal zero')
elif x < 20:
	print('x is 20')
elif x == 10:
	print('x is 10')
else:
	print(' x is nothing')


x = 90
y = 45

if x == y:
	print('x and y are equal')
elif x > y:
	print('x is greater than y')
else:
	print('x is Less than y')


#Shorthand ifelif

if x < y: print('x is less than y')

x = 50
y = 150
print(x) if x > y else print(y)

# AND is logical operator

x = 50
y = 40
z = 100
if x > y and z > y or x > z:
	print('All conditions are true')
else:
	print('one condition is true')


# nested if else 

x = 50
if x > 10:
	print('x is greater----------- than ten')
	if x > 20:
		print('x is greater than 20')
		if x > 40 and x < 50 or x ==50:
			print('x is above 40 or equal to 50')
		else:
			print('x is normal')
	else:
		print ('No, x is not greater than 20')
else:
	print('x is smaller than 10')


int(input("Examination result: "))

100 - 90			-A
90  - 70			-B
70  - 60			-C
60  - 40 			-D
40  -  0			-Fail