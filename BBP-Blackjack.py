""" 
Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version 
doesn't have splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, card game
"""

import random, sys

# Set un the constants:
HEARTS      = chr(9829)  # Character 9829 is '♥'.
DIAMONDS    = chr(9830)  # Character 9830 is '♦'.
SPADES      = chr(9824)  # Character 9824 is '♠'.
CLUBS       = chr(9827)  # Character 9827 is '♣'.
BACKSIDE    = 'backside'

def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
    money = 5000
    # Main game loop.
    while True:
        # Check if the player still has money.
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Let the player enter their bet for this round:
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deach each.
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        # Keep looping until the player stands or busts.
        while True: 
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust.
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, hit, stand, or double down.
            move = getMove(playerHand, money - bet)

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet.
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                #Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break

        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits.
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    # The dealer has busted.
                    break
                input('Press Enter to continue...')
                print('\n\n')


        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input ('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    """
    Asks the player how much they want to bet for this round.
    """
    # Loop to ask until a valid amount is entered.
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            # If the player didn't enter a number, ask again.
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet
        
def getDeck():
    """
    Return a list of (rank, suit) tuples for all 52 cards.
    """

    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """
    Show the player's and dealer's cards. Hide the dealer's first card
    if showDealerHand is False.
    """

    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """
    Returns the value of the cards. Face cards are worth 10, aces are 
    worth 11 or 1 (this function picks the most suitable ace value).
    """

    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank) 

    # Add the value for the aces:
    value += numberOfAces 
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10
    
    return value


def displayCards(cards):
    """
    Display all the cards in the cards list.
    """

    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Print the card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """
    Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down.
    """
    # Keeps looping until the player enters a correct move.
    while True:
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we
        # can tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move
        

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()