#Number Guessing Game (Basic)
num = 7
guess = int(input("Guess the number between 1 to 10: "))

if guess == num:
    print(f"{guess} Correct! You guessed the number.")

else:
    print(f"{guess} Wrong! You guessed the wrong number. Please try again.")


#Output
"""
1. Guess the number between 1 to 10: 5
5 Wrong! You guessed the wrong number. Please try again. 

2. Guess the number between 1 to 10: 7
7 Correct! You guessed the number.
"""