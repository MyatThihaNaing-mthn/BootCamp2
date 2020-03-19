# Keyboard Interrupt

while True:
	try:
		x = int(input("Please enter a number:"))
		print(x)
		break
	except ValueError:
		print("Oops! That was no valid number, Try again...")

-------------------------------------------------

#OSError , Value Error

import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OSError: {0}".format(err))
except ValueError:
	print("Could not invert data to an integer.")
except:
	print("Unexpected error:", sys.exc_info[0])
	raise

-------------------------------------------------------------

# EOF errror, keyboard Interrupt

try:
	text = input("enter something --->")
except EOFError:
	print("Why did you do an EOF on me?")
except KeyboardInterrupt:
	print('You cancelled the operation.')
else:
	print("You entered.{}".format(text))

-------------------------------------------------------------------


# Raise Exceptions

class ShortInputException(Exception):
	'''A user-defined exception class'''

	def __init__(self, length, atLeast):
		Exception.__init__(self)
		self.length = length
		self.atLeast = atLeast

		try:
			text = input("Enter something -->")
			if (len(text)) < 3:
				raise ShortInputException(len(text), 3)
				# other work can continue as usual here
		except EOFError:
			print("Why did you do an EOF on me?")
		except ShortInputException as ex:
			print(('ShortInputException: The input was'+ '{0} long, excepted at least {1}').format(ex.length, ex.atLeast))
		else:
			print("No exception was raised")


# Try.... Finally

import sys
import time

f = None
try:
	f = open("poem.txt")

	#our usual file reading idiom

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end ="")
		sys.stdout.flush()
		print("press ctrl+c now")

		# To make it run for a while

		time.sleep(2)

except IOError:
	print("Could not find file poem.txt")

except KeyboardInterrupt:
	print("!! You cancelled the reading form the file")

finally:
	if f:
		f.close()
		print("(Cleaning up:: closed the file")