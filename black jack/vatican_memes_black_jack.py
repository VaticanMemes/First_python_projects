import random

cards = [["clubs", "spades", "diamonds", "hearts"], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "king", "queen", "ace"]]

value = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "king": 10, "queen": 10, "ace": 11}

def get_cards():
    your_cards = []
    for i in range(2):
        individual_card = []
        individual_card.append(cards[1][random.randint(0, 11)])
        individual_card.append(cards[0][random.randint(0, 3)])
        your_cards.append(individual_card)
    printable_cards = []
    for i in your_cards:
        printable_cards.append(" of ".join(i))
    return your_cards, printable_cards

def get_dealers_card():
     individual_card = []
     printable_cards = []
     dealers_cards = []
     individual_card.append(cards[1][random.randint(0, 11)])
     individual_card.append(cards[0][random.randint(0, 3)])
     dealers_cards.append(individual_card)
     printable_cards.append(" of ".join(individual_card))
     return dealers_cards, printable_cards


def get_total(your_cards):
    count = 0
    for i in your_cards:
        count += value[i[0]]
    return count

def hit_or_stand(your_cards):
    h_or_s = input("Hit or stand? (h/s) ")
    if h_or_s == "h":
        individual_card = []
        individual_card.append(cards[1][random.randint(0, 11)])
        individual_card.append(cards[0][random.randint(0, 3)])
        your_cards.append(individual_card)
        printable_cards = []
        for i in your_cards:
                printable_cards.append(" of ".join(i))
        return your_cards, printable_cards, "hit"
    elif h_or_s == "s":
        printable_cards = []
        for i in your_cards:
                printable_cards.append(" of ".join(i))
        return your_cards, printable_cards, "stand"
    else:
        print("Pick enter a valid input.")
        hit_or_stand(your_cards)

def play_or_nay():
    pl_or_na = input("Would you like to play? (y/n) ")
    if pl_or_na == "y":
         pass
    elif pl_or_na == "n":
         quit()
    else:
         print("Please enter a valid input.")
         play_or_nay()

def beginnings():
    print("Welcome to blackjack!")
    play_or_nay()
    your_cards, printable_cards = get_cards()
    printable_cards = ", ".join(printable_cards)
    print(f"Your cards are: {printable_cards}")
    print(f"Total: {get_total(your_cards)}")
    dealers_card, printable_dealers_card = get_dealers_card()
    printable_dealers_card = "".join(printable_dealers_card)
    print(f"Dealers card: {printable_dealers_card}")
    print(f"Dealers total: {get_total(dealers_card)}")
    return your_cards, dealers_card

def finale(your_cards, dealers_card):
     while get_total(dealers_card) < 18:
        dealers_individual_card = []
        dealers_printable_card = []
        dealers_individual_card.append(cards[1][random.randint(0, 11)])
        dealers_individual_card.append(cards[0][random.randint(0, 3)])
        dealers_card.append(dealers_individual_card)
        for i in dealers_card:
            dealers_printable_card.append(" of ".join(i))
        dealers_printable_card = ", ".join(dealers_printable_card)
     print(f"Dealers cards: {dealers_printable_card}")
     print(f"Dealers total: {get_total(dealers_card)}")
     if get_total(dealers_card) > 21:
          print("Dealer busts. You win!")
          print()
          main()
     elif get_total(your_cards) > get_total(dealers_card):
          print("You win!")
          print()
          main()
     elif get_total(your_cards) < get_total(dealers_card):
          print("Dealer wins.")
          print()
          main()
     elif get_total(your_cards) == get_total(dealers_card):
          print("Draw.")
          print()
          main()

def the_loop(your_cards, dealers_card):
    your_cards, printable_cards, h_s_output = hit_or_stand(your_cards)
    printable_cards = ", ".join(printable_cards)
    print(f"Your cards are: {printable_cards}")
    print(f"Total: {get_total(your_cards)}")
    if get_total(your_cards) > 21:
         print("You bust. Dealer wins.")
         print()
         main()
    if h_s_output == "stand":
         pass
         finale(your_cards, dealers_card)
    the_loop(your_cards, dealers_card)

def main():
    your_cards, dealers_card = beginnings()
    the_loop(your_cards, dealers_card)

main()
