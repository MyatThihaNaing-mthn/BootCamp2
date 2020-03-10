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