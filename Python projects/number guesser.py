import random

while True:

    guesses = 0

    while True:

        print("            Random number generator")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        while True:
            lower_range = input("Pick the smallest number you can think of: ")
            if lower_range.isdigit():
                lower_range = int(lower_range)
                break
            else:
                print("Please pick a number...")
                continue

        while True:
            upper_range = input("Pick the largest number you can think of: ")
            if upper_range.isdigit():
                upper_range = int(upper_range)
                break
            else:
                print("Please pick a number...")
                continue

        if upper_range > lower_range:
            number = random.randint(lower_range, upper_range)
            print("You have just generated a random number from {int(lower_range)}} to {int(upper_range)}. Now your task is to guess it!")
            break
        else:
            print("You're a funny guy. Your lowest number needs to be lower than largest number.")
            continue

    while True:
        guesses += 1
        guess = input("Please guess a number: ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Do a number next time.")
            continue

        if guess == number:
            print("You won!!! You got it in {int(guesses)}.")
            break
        else:
            print("Guess again")
            continue
    
    continue