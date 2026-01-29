import random
number=random.randint(1,100)
attempts=0

while True:
    guess=int(input("Guess a number between 1 and 100: "))
    attempts+=1
    if guess<number:
        print("Too low! Try again")
    if guess>number:
        print("Too high! Try again")
    if guess==number:
        print("Wow! You guessed it correctly")
        print("Total attempts:", attempts)
        break


# OUTPUT:
Guess a number between 1 and 100: 56
Too low! Try again
Guess a number between 1 and 100: 78
Too low! Try again
Guess a number between 1 and 100: 92
Too high! Try again
Guess a number between 1 and 100: 90
Too low! Try again
Guess a number between 1 and 100: 91
Wow! You guessed it correctly
Total attempts: 5


