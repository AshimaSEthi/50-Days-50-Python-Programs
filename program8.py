#convert string input entered to integer first
input_entered = int(input("Enter the Number to be checked: "))


#we need to use if else loop
if input_entered >0:
	print("The number entered is positive")
elif input_entered <0:
	print("The number entered is negative")
else:
	print("The number entered is zero")