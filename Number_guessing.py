import random

i = 1
while i <= 5 :

	attempts = 5
	guess = input("Enter your guess: ")
	number = random.randint(0,1)
	print(number)
	if number == int(guess) and attempts != 0:
		print("Your guess "+ str(number) + " is correct.")
		break
	elif number != guess and attempts !=0:
	 	print("Your guess was incorrect.")
	 	print("\n")
	 	attempts = attempts - i 
	 	print("You still have " + str(attempts) + " attempts left.")
	elif number != guess and attempts == 0:
	 	print("Your guess was incorrect.")
	 	print("\n")
	 	print("You are out of attempts")	 	
	i += 1