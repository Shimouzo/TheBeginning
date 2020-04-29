import random

num = int((random.uniform(0, 20)))
guess = ""

while guess != num:
    try:
        guess = input(str("Guess a number between 0 and 20: "))
        if int(guess) > int(num):
            print("Your guess is too high, try again.")
        elif int(guess) < int(num):
            print("Your guess is too low, try again.")
        else:
            print("Correct!")
            break
    except ValueError:
        print(guess + " is not a number.")
