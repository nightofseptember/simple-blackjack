import random


# cards get handed out
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Calculates each hand
def total(turn):
    total = 0
    ace_11s = 0
    for card in turn:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:  #No idea how this shi works it was just a fix i found
        total -= 10
        ace_11s -= 1
    return total    

# checks for winner
def showDealerHand(): #vshows dealerhand
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
        dealCard(dealerHand)
        dealCard(playerHand)

    while playerIn or dealerIn:
        print(f"Dealer has {dealerHand} for a total of {total(dealerHand)}")
        print(f"You have {playerHand} for a total of {total(playerHand)}")

# Player turn
        if playerIn:
            stayOrHit = input("1: Stay\n2: Hit\n")
            if stayOrHit == '1':
                playerIn = False
            else:
                dealCard(playerHand)
            if total(playerHand) >= 21:
                break

# Dealer turn
        if dealerIn:
            if total(dealerHand) > 17:
                dealerIn = False
            else:
                dealCard(dealerHand)
# If bust no dice
        if total(playerHand) >= 21 or total(dealerHand) >= 21:
            break

    if total(playerHand) == 21:
        print(f"\You have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("BLACKJACK! you won")
    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("2")
    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("3")
    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")    
        print("4")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
        print("5")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
        print("6")




    playAgain = input("\nDo you wanna play again (Yes/No): ").lower()
    if playAgain != 'yes':
        print("Well played, see you next time.")
        break  # Exit the loop to end the game