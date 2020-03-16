# with open('test.pptx', 'rb') as rf:
# 	with open('testCOPY.pptx','wb') as wf:

# 		for line in rf:
# 			wf.write(line)

with open('cat.jpg', 'rb') as rf:
	with open('cat_copy.png', 'wb') as wf:
		for line in rf:
			wf.write(line)