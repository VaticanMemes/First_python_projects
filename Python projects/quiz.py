score = 0

print("Welcome to... ")
print("              the quiz")
print("You are being tested.")

play1 = input("Are you sure you want to go ahead? ")

if play1.lower() != "yes":
    quit()

play2 = input("Are you sure you're sure? ")

if play2.lower() != "yes":
    quit()

print("Whatever you say boss...")

answer1 = input("Capital of Alabama? ")
if answer1.lower() == "montgomery":
    print("Correct!")
    score += 1
else:
    print("Montgomery you dumb cunt!")

answer2 = input("Who's the most handsome of them all? ")
if answer2.lower() == "daniel craig":
    print("Correct!")
    score += 1
else:
    print("Daniel Craig you dumb cunt!")

answer3 = input("A black and a mexican are in a car. Who's driving? ")
if answer3.lower() == "the cops":
    print("Correct!")
    score += 1
else:
    print("The cops you dumb cunt!")

if score == 3:
    print("You got " + str(score) + "/3. Which is " + str((score/3) * 100) + "%. Nothing wrong for Mr Wong.")
else:
    print("You got " + str(score) + "/3. Which is " + str((score/3) * 100) + "%. You've dropped a couple IQ points.")