import random
from char_database import chars, chars1, chars2, chars3

try:
    lim = 0
    dif = int(input("Enter how complicated do you want your password to be on a scale from 0 to 3: "))

    if dif == 0:
        num_of_chars = int(input("Number of characters in your password: "))
        while lim != num_of_chars:
            print(random.choice(chars), end="")
            lim += 1
    elif dif == 1:
        num_of_chars = int(input("Number of characters in your password: "))
        while lim != num_of_chars:
            print(random.choice(chars1), end="")
            lim += 1
    elif dif == 2:
        num_of_chars = int(input("Number of characters in your password: "))
        while lim != num_of_chars:
            print(random.choice(chars2), end="")
            lim += 1
    else:
        num_of_chars = int(input("Number of characters in your password: "))
        while lim != num_of_chars:
            print(random.choice(chars3), end="")
            lim += 1
except ValueError:
    print("That is not a number")
