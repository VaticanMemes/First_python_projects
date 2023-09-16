while True:
    name = input("What is your name: ")
    print(f"Welcome {name} to this adventure.")
    while True:
        answer1 = input("Would you like to recieve the magic sword? ")
        if answer1.lower() == "yes":
            print("You are greedy. You lose.")
            break
        if answer1.lower() == "no":
            while True:
                answer2 = input("Good job. You find some thugs. Should you stab them? ")
                if answer2.lower() == "yes":
                    print("Unlucky boss, you just got stabbed by British lads. You lose.")
                    break
                if answer2.lower() == "no":
                    print("You're a wimp. You lose.")
                    break
                else:
                    print("Type either 'yes' or no'.")
                    break
        else:
            print("Type either 'yes or 'no.")
            continue
        break