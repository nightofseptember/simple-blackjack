import random


#kort delt ut
def delKort(tur):
    kort = random.choice(deck)
    tur.append(kort)
    deck.remove(kort)

# lkalkulerer hånd
def total(tur):
    total = 0
    ace_11s = 0
    for kort in tur:
        if kort in range(11):
            total += kort
        elif kort in ['10', '10', '11']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:  #No idea how this shi works it was just a fix i found
        total -= 10
        ace_11s -= 1
    return total    

# sjekker for vinner
def visForhandlerHånd(): #vshows dealerhand
    if len(forhandlerhånd) == 2:
        return forhandlerhånd[0]
    elif len(forhandlerhånd) > 2:
        return forhandlerhånd[0], forhandlerhånd[1]
# loop
while True:
    playerIn = True
    dealerIn = True
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, '10', '10', '10', '11'] * 4
    spillerhånd = []
    forhandlerhånd = []

    for _ in range(2):
        delKort(forhandlerhånd)
        delKort(spillerhånd)

    while playerIn or dealerIn:
        print(f"Forhandler har {forhandlerhånd} {total(forhandlerhånd)}")
        print(f"Du har {spillerhånd} for en total av {total(spillerhånd)}")

#spiller tur
        if playerIn:
            stayOrHit = input("1: Stay\n2: Hit\n")
            if stayOrHit == '1':
                playerIn = False
            else:
                delKort(spillerhånd)
            if total(spillerhånd) >= 21:
                break

# forhandler sin tur
        if dealerIn:
            if total(forhandlerhånd) > 17:
                dealerIn = False
            else:
                delKort(forhandlerhånd)
# hvis du buster no dice
        if total(spillerhånd) >= 21 or total(forhandlerhånd) >= 21:
            break

    if total(spillerhånd) == 21:
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")
        print("BLACKJACK! du vant")
    elif total(forhandlerhånd) == 21:
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")
        print("2")
    elif total(forhandlerhånd) > 21:
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")
        print("Forhandler busta, Du vant")
    elif total(forhandlerhånd) > 21:
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")    
        print("4")
    elif 21 - total(forhandlerhånd) < 21 - total(spillerhånd):
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")  
        print(f"\nForhandler vant siden han har {total(forhandlerhånd)}")
    elif 21 - total(forhandlerhånd) > 21 - total(spillerhånd):
        print(f"\nDu har{spillerhånd} for en total av {total(spillerhånd)} og forhandleren har {forhandlerhånd} for en total av {total(forhandlerhånd)}")  
        print("Du busta, dealer vant")


# hva gjør f"\n??

    spillIgjen = input("\nVill du spille igjen (Ja/Nei):? ").lower()
    if spillIgjen != 'ja':
        print("Bra spilt ses igjen")
        break  # Exit the loop to end the game