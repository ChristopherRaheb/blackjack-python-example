import random

# create deck in the form of a 2D array
# card arrays each include a value and a suit
def createDeck():
    deck = []
    i = 0
    value = 1
    while i < 52:
        if value == 1:
            newVal = "Ace"
        elif value == 11:
            newVal = "Jack"
        elif value == 12:
            newVal = "Queen"
        elif value == 13:
            newVal = "King"
        else:
            newVal = value
        if i < 13:
            suit = "Hearts"
        elif i < 26:
            suit = "Spades"
        elif i < 39:
            suit = "Clubs"
        else:
            suit = "Diamonds"
        newList = [newVal,suit]
        deck.append(newList)
        i += 1
        if value != 13:
            value += 1
        else:
            value = 1
    return deck

# print a deck or hand
def showDeck(deck):
    for card in deck:
        print(card[0], "of", card[1])
    print()

# deal a card from a deck
def deal(deck):
    card = deck.pop(0)
    return card

# create a hand array and deal a card to it
def createHand(deck):
    hand = []
    hand.append(deal(deck))
    return hand

# get the point value of a hand
def getPoints(hand):
    points = 0
    for card in hand:
        newPoint = card[0]
        if newPoint == "Jack" or newPoint == "Queen" or newPoint == "King":
            newPoint = 10
        elif newPoint == "Ace":
            if points + 11 > 21:
                newPoint = 1
            else:
                newPoint = 11
        points += newPoint
    return points

# read money from file
# if no file then creates one with a starting value of 1000
def getMoney():
    try:
        moneyTest = open("money.txt", "r")
    except Exception:
        print("Data file missing, resetting starting amount to 1000.")
        with open("money.txt", "w") as file:
            file.write(1000)
    finally:
        with open("money.txt") as file:
            money = file.read()
            if money == "":
                money = 1000.0
            money = float(money)
            if money < 5:
                money = 1000.0
                print("Money is less than 5. New money amount:", money)
            return money
        
# user sets their bet amount
def setBet(money):
    valid = False
    while(valid == False):
        try:
            response = float(input("Bet amount: "))
        except Exception:
            print("Invalid amount, try again.")
            continue
        if(response < 5):
            print("The minimum bet is 5. Please try again.")
        elif(response > 1000):
            print("The maximum bet is 1000. Please try again.")
        elif(response > money):
            print("You don't have enough to cover that bet. Please try again.")
        else:
            return response

# the player's turn, allows them to hit or stand
def playerTurn(bet, deck, playerHand):
    choice = input("Hit or stand? (h/s): ")
    while choice.lower() == "h":
        if getPoints(playerHand) > 21:
            break
        else:
            playerHand.append(deal(deck))
            print("\nYOUR CARDS:")
            showDeck(playerHand)
            if getPoints(playerHand) > 21:
                break
            choice = input("Hit or stand? (h/s): ")

# determines if the player loses, wins, or ties
def outcome(money, bet, playerHand, dealerHand):
    if (getPoints(playerHand) > getPoints(dealerHand) and getPoints(playerHand) <= 21) or getPoints(dealerHand) > 21:
        print("\nYou win!")
        money = float(money + bet)
        with open("money.txt", "w") as file:
            file.write(str(money))
        print()
    elif getPoints(playerHand) < getPoints(dealerHand) or getPoints(playerHand) > 21:
        print("\nSorry. You lose.")
        money = float(money - bet)
        with open("money.txt", "w") as file:
            file.write(str(money))
        print("Money:", money)
        print()
    else:
        print("\nYou tied.")

# the main game loop
def game(money):
    response = "y"
    while response.lower() == "y":
        bet = setBet(money)
        print()
        deck = createDeck()
        random.shuffle(deck)
        playerHand = createHand(deck)
        playerHand.append(deal(deck))
        dealerHand = createHand(deck)
        print("DEALER'S SHOW CARD:")
        showDeck(dealerHand)
        print("YOUR CARDS:")
        showDeck(playerHand)
        playerTurn(bet, deck, playerHand)
        dealerHand.append(deal(deck))
        while getPoints(dealerHand) <= 16:
            dealerHand.append(deal(deck))
        print("\nDEALER'S CARDS:")
        showDeck(dealerHand)
        print("YOUR CARDS:")
        showDeck(playerHand)
        print("YOUR POINTS: ", getPoints(playerHand))
        print("DEALER'S POINTS:", getPoints(dealerHand))
        outcome(money, bet, playerHand, dealerHand)
        response = input("Play again? (y/n): ")
        print()

# main function
def main():
    print("BLACKJACK!\nBlackjack payout is 3:2\n")
    money = getMoney()
    print("Money:", money, "\n")
    game(money)
    print("Come back soon!\nBye!")

# runs main function
if __name__ == "__main__":
    main()
