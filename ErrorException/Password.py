class PasswordException(Exception):
	"""A user-defined exception class"""

	def __init__(self, length, atLeast, atMost):
		Exception.__init__(self)
		self.length = length
		self.atLeast = atLeast
		self.atMost = atMost


try:
	text = int(input('Enter something -->'))

	if len(str(text)) < 7:
		raise ShortInputException(len(str(text)), 7)

	if len(str(text)) > 12:
		raise LongInputException(len(str(text)), 12)
		


except ValueError:
	print("Input was not integer")

except EOFError:
	print("Why did you do an EOF on me?")

except KeyboardInterrupt:
	print("!! You canceled the reading from the file.")

except ShortInputException as sx:
	print(('ShortInputException: The input was'+ '{0} long, excepted at least {1}').format(sx.length, sx.atLeast))

except LongInputException as lex:
	print(('LongInputException: The input was'+ '{0} long, excepted at most {1}').format(lex.length, lex.atMost))

else:
	print("No exception was raised")