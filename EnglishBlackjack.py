import random


# cards get handed out
def delKort(tur):
    kort = random.choice(deck)
    tur.append(kort)
    deck.remove(kort)

# Calculates each hand
def total(tur):
    total = 0
    ace_11s = 0
    for kort in tur:
        if kort in range(11):
            total += kort
        elif kort in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total

# checks for winner
def visDealerHand(): #vshows dealerhand
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
# loop
while True:
    playerIn = True
    dealerIn = True
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    playerHand = []
    dealerHand = []

    for _ in range(2):
        delKort(dealerHand)
        delKort(playerHand)

    while playerIn or dealerIn:
        print(f"Dealer has {visDealerHand()}")
        print(f"You have {playerHand} for a total of {total(playerHand)}")

# Player turn
        if playerIn:
            stayOrHit = input("1: Stay\n2: Hit\n")
            if stayOrHit == '1':
                playerIn = False
            else:
                delKort(playerHand)
            if total(playerHand) >= 21:
                break

# Dealer turn
        if dealerIn:
            if total(dealerHand) > 17:
                dealerIn = False
            else:
                delKort(dealerHand)
# If bust no dice
        if total(playerHand) >= 21 or total(dealerHand) >= 21:
            break

    if total(playerHand) == 21:
        print(f"\You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack!")
    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You busted, Dealer Won")
    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You busta, Dealer vant")
    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")    
        print("Dealer busted, You won")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
        print("dealer won")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
        print("Du won")




    spilleIgjen = input("\nDo you wanna play again (Yes/No): ").lower()
    if spilleIgjen != 'yes':
        print("Well played, see you next time.")
        break  # Exit the loop to end the game