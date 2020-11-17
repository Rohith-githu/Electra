def game() :
	import random
	number = random.randint(1,9)
	for num in range(3) :
		guess = int(input('enter the guess'))
		if guess == number :
			print('you had entered the correct guess')
			exit()
		elif guess != number :
			print('you had entered the wrong guess')
	print('you are out of tries')
	print(f'{number} is the correct guess')
