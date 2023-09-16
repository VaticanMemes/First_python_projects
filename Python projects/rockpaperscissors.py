import random

options = ["rock", "paper", "scissors"]
wins = 0
draws = 0
loses = 0

while True:
    enemy = random.randint(1, 3)
    print("             Python rock paper scissors!!!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    move = input("Rock, paper, or scissors? Or 'q' to quit. ").lower()
    if move == "q":
        print("You won " + str(wins) + " times.")
        print("You drew " + str(draws) + " times.")
        print("You lost " + str(loses) + " times.")
        quit()
    elif move not in options:
        print("Please learn to follow instructions.")
        continue
    else:
        randnum = random.randint(0, 2)
        # Rock: 0
        # Paper: 1
        # Scissors: 2
        enemy = options[randnum]
        print("Your worst enemy picked " + enemy + ".")

        if move == "rock" and enemy =="scissors":
            wins += 1
            print("Good job. You have won " + str(wins) + " times.")
            continue

        if move == "scissors" and enemy =="paper":
            wins += 1
            print("Good job. You have won " + str(wins) + " times.")
            continue

        if move == "paper" and enemy =="rock":
            wins += 1
            print("Good job. You have won " + str(wins) + " times.")
            continue

        if move == enemy:
            draws += 1
            print("You drew. You have drawn " + str(draws) + " times.")
            continue

        else:
            loses += 1
            print("You lost son. You have lost " + str(loses) + " times.")
            continue