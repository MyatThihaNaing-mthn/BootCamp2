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