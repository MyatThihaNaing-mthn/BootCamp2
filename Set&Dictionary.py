Set&Dictionary.py

#Sets

includes a data type for sets.
Curly braces or the set() fucntion can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket
'crabgrass' in basket

Demonstrate set operations on unique letters from two words.

a = set('abracadabra')
b = set('alacazam')

a 		#unique letters in a
a - b 	#letters in a but not in b
a | b 	#letters in a or b or both
a & b 	#letters in both a and b
a ^ b 	#letters in a or b but not both

#>> Dictionaries

#another useful data type built into python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

---------

del tel['sape']
tel['irv'] = 4137
tel

list(tel)

sorted(student) # alphabet sorting

'MgOo' in student
'MaMa' in student

-------------

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape = 4139, guido = 4127, jack = 4098)

#when looping through Dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'sape': 4355}
for x, y in knights.items():
	print(x, y)


for x, y in enumerate(['tic','tac','toe']):
	print(x, y)

------------
#sum
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
	print('What is your{0}? It is {1}.' .format(q, a))


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
result = [1, 2, 3]

for q, a in zip(questions, answers, result):
	print('What is your{0}? It is {1}.It is {2}' .format(q, a, i))

---------------
print('{0} and {1}, {2} '. format('spam','eggs', 'color', 'food'))
