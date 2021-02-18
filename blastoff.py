
#This is where the functions for countdown and countup are defined when the program starts.
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
#The countup function is set to check for when the number in the count reaches 0 before printing "Blastoff!".
def countup(n):
	if n >= 0:
		print('Blastoff!')
	else:
		print(n)
		countup(n+1)


#The code for the Input, which is how the code receives the number.
number = int(input("Enter a positive or negative number: "));
if number < 0:
    countup(number)
elif number > 0:
    countdown(number)
elif number == 0:
    countup(number)
else:
    print('Input not accepted.');



