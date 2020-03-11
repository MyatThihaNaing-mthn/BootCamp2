x = int (input("Enter the correct exam result: "))

if x <= 100 and x >= 90:
	print('A')
elif x <= 89 and x >= 70:
	print('B')
elif x <= 69 and x >= 60:
	print('C')
elif x <= 59 and x >= 40:
	print('D')
elif x <= 39 and x >= 0:
	print('FAIL')
else: 
	print('Please enter the correct exam result...')