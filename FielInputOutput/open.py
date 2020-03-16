# Create FIleInputOutput into Python Code
# save as Open.py in FIleInputOutput

# "r" = read
# "a" = append
# "w" = write
# "x" = Create
# "t" = Text
# "b" = Binary

# open & Read FIleInputOutput
# f = open('test.txt', 'r') # R - Read
# print(f.name)
# f.close()


# with open('test.txt', 'a' ) as f:
# 		f.write('This is line number' + "\n")
# 		print(f, end='')

with open('test.txt', 'r') as f:
	f_text = f.readline()
	print(f_text, end ='')

# 	f_text = f.readline()
# 	print(f_text, end ='')

# # 	f_text = f.readline()
# # 	print(f_text, end ='')

	# for x in f:
	# 	print(x, end='')

	f_text = f.read(10)
	print(f_text, end='')

# # 	f_text = f.read(100)

# # 	while 100 > 0:
# # 		print(f_text, end = '')