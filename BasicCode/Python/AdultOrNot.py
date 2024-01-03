age = int(input("Please enter your age: "))
if age <= 0:
	print('Invalid input')
elif age >= 1 and age <= 5:
	print('Infant')
elif age >= 6 and age <= 10:
	print('Child')
elif age >= 11 and age <= 17:
	print('Teenager')

else:
	print('Adult')
