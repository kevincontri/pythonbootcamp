import random
"""Blackjack simulation in Python"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1, 'Ace2': 11}


class Card:
    """Each card has a suit, a rank and it's corresponding value, according to the dictionary above"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """A deck made of 52 cards, all possible combinations between the suits and ranks available"""

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                individual_card = Card(suit, rank)

                self.all_cards.append(individual_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
        print("Cards shuffled!")

    def pop_card(self):
        return self.all_cards.pop()


class Player:
    """
    Each player has a name, a bankroll and a list with all the cards currently on their hands.
    The deal() method takes two arguments:
        - The deck in with the card will be popped out
        - The specified quantity of cards to be popped out
    It has a special rule that, once the card taken is of rank 'Ace', it will prompt the user to
    choose between the value of 1 or 11, the one the user prefers.
    After that, it appends that card to user's hands.

    The clear_hand() method clears or empty the list of cards of the player's hand, therefore resetting
    the game in case the player replays.
    """

    def __init__(self, name, bankroll_amount):
        self.name = name.capitalize()
        self.bankroll = bankroll_amount
        self.hand = []

    def __str__(self):
        return f"Player: {self.name}\nBankroll: {self.bankroll}\n"

    def deal(self, deck, qty):
        for x in range(qty):
            card_dealt = deck.pop_card()
            if card_dealt.rank == 'Ace':
                val = 'wrong'
                while val not in [1, 11]:
                    val = int(input(f"You've got: {card_dealt}, count it's value as 1 or 11? "))
                if val == 11:
                    card_dealt.value = values['Ace2']
                else:
                    card_dealt.value = values['Ace']
            self.hand.append(card_dealt)
        print("{} card(s) dealt to {}!".format(qty, self.name))

    def clear_hand(self):
        self.hand = []


class Dealer:
    """
    The Dealer is essentially the computer, but in the game context, it represents the Casino itself.
    It's bankroll value is set to 0, for as the player lose, the Dealer's (Casino's) bankroll increases.
    The deal() method is similar to the Player's one, but without the possibility to choose values in case
    of an Ace rank, in which case here Ace counts as 11 unless it would bust, then it counts as 1.
    The clear_hand() method works the same as the Player's.
    """

    def __init__(self, name="Dealer"):

        self.name = name
        self.bankroll = 0
        self.hand = []

    def deal(self, deck, qty):
        for x in range(qty):
            card_dealt = deck.pop_card()
            if card_dealt.rank == 'Ace':
                total_value = 0
                for card in self.hand:
                    total_value += card.value
                if (total_value + 11) <= 21:
                    card_dealt.value = values['Ace2']
                else:
                    card_dealt.value = values['Ace']
            self.hand.append(card_dealt)
        print("{} card(s) dealt to the Dealer!".format(qty))

    def clear_hand(self):
        self.hand = []


"""
The player_bet() function receives as argument the player object, and asks the player the value of their bet for that set of hands (turn),
And makes some validation as:
- Makes sure the player's bankroll is not zero
- Makes sure the player types an integer
- Makes sure the player's bet is less than their current bankroll
It returns the value of their bet
"""


def player_bet(player):
    if player.bankroll == 0:
        print("I'm sorry, it seems like your bankroll is empty! That's bad!")
        return 0
    bet = 'wrong'
    bank = player.bankroll
    while type(bet) != type(0):
        try:
            bet = int(input(
                f"{player.name}, your current bankroll is {player.bankroll}.\nWhat's your bet for this set of hands? "))
        except ValueError:
            print("\nInvalid bet value! \n")
            continue

    while bet > bank or bet <= 0:
        try:
            bet = int(input("\nInvalid value! Insert new bet: "))
        except:
            continue

    return bet


"""
The hit_or_stay() function asserts the action the player will do once they perceive they need to
HIT, which means add one more card to their hand, or Stay, meaning to stop receiving cards and
betting the one's on their hands are enough.
Also, it has some validation for the response.
"""


def hit_or_stay(player):
    action = 'wrong'
    while action not in ['hit', 'stay']:
        action = input(f"\n{player.name}, Hit or Stay? ").lower()

        if action not in ['hit', 'stay']:
            print("Invalid action!")

    return action


"""
A bust in Blackjack means a player's hand total sum is greater than 21. Meaning either the player
lost of the dealer lost.
"""


def bust(player_or_dealer):
    total_value = 0
    for card in player_or_dealer.hand:
        total_value += card.value

    return total_value > 21


"""
Helper function to make sure the player or the dealer still have their hand's total value less than 21
"""


def under_21(player_or_dealer):
    total_value = 0
    for card in player_or_dealer.hand:
        total_value += card.value

    if total_value < 21:
        return True, total_value
    else:
        return False, total_value


def tie(player, dealer):
    player_total = 0
    for Pcard in player.hand:
        player_total += Pcard.value

    dealer_total = 0
    for Dcard in dealer.hand:
        dealer_total += Dcard.value

    return player_total == dealer_total


"""
The proper game!
This how each line of code works:
- Start with a shuffled deck of 52 cards
- Ask the player for their bet value, making sure of their bankroll
- Clear player's hand, to a fresh start
- The dealer and the player takes two cards from the deck.
- It's displayed just one card of the dealer (One faced-up, other faced-down)
- It's displayed both the player cards
- Ask the player if they want to HIT or STAY
- If they HIT, they receive one more card from the deck, and displays it.
- Checks whether the player already has the value 21, in which case the player wins,
  or they faced a BUST, in which case the Dealer wins. Or if their values are the same (A tie)
- If it was not a BUST, the player is asked again if they HIT or STAY.
- Once the player STAYS, it is shown the dealers faced-down card.
- Now in the dealer's turn, if their current value is less than the player's, it increases
  one card at a time.
- Checks whether the dealer faced a BUST (Player wins) or
  if the the total sum of their card values equals 21 (Dealer wins), if neither is true,
  it keeps hitting. Or if their values are the same (A tie)
- If the dealer reaches a value greater than the player's, and it's still under 21, then
  the dealer wins, otherwise, the dealer lose.
"""


def game():
    game_on = True
    deck = Deck()

    while game_on:
        deck.shuffle()
        bet = player_bet(player)
        if bet == 0:
            print("See you next time!")
            return
        dealer.clear_hand()
        player.clear_hand()
        print("\n"*60)
        dealer.deal(deck, 2)
        player.deal(deck, 2)
        Dcard1, Dcard2 = dealer.hand
        Pcard1, Pcard2 = player.hand
        print(f"Dealer's cards: | {Dcard1} | XX |")
        print(f"Player's cards: | {Pcard1} | {Pcard2} |")

        dealer_turn = False
        player_turn = True
        while player_turn:
            player_action = hit_or_stay(player)
            if player_action == 'hit':
                player.deal(deck, 1)
                if tie(player, dealer):
                    print("It's a tie!")
                    player_turn = False
                    game_on = False
                    break
                player_under21, player_value = under_21(player)
                print(f"{player.name}'s new card: | {player.hand[-1]} |")
                if player_value == 21:
                    print(f"\nThat's a BlackJack! {player.name} won in the first round!\n")
                    player.bankroll += bet * 2
                    print(f"{player.name}'s bankroll: {player.bankroll} chips")
                    player_turn = False
                    game_on = False
                    break
                if not bust(player):
                    continue
                else:
                    print("\nIt's a BUST, Dealer wins!")
                    dealer.bankroll += bet
                    player.bankroll -= bet
                    print(
                        f"Casino received: {bet} chips\nPlayer's bankroll: {player.bankroll} chips\n")
                    player_turn = False
                    game_on = False
                    break
            else:
                print(f"\nDealer's faced down card: | {Dcard2} |\n")
                if Dcard1.value + Dcard2.value == 21:
                    print(f"\nThat's a BlackJack! {dealer.name} won in the first round!\n")
                    dealer.bankroll += bet
                    print(
                        f"Casino received: {bet} chips\nPlayer's bankroll: {player.bankroll} chips")
                    player_turn = False
                    game_on = False
                    break
                player_turn = False
                dealer_turn = True

        while dealer_turn:
            player_under21, player_value = under_21(player)
            dealer_under21, dealer_value = under_21(dealer)

            if player_under21:
                while dealer_value < player_value:
                    dealer.deal(deck, 1)
                    if tie(player, dealer):
                        print("It's a tie!")
                        dealer_turn = False
                        game_on = False
                        break
                    print(f"\nNew {dealer.name} card: | {dealer.hand[-1]} |\n")
                    if dealer_value == 21:
                        print("\nDealer wins!")
                        dealer.bankroll += bet
                        player.bankroll -= bet
                        print(
                            f"Casino received {bet} chips\nPlayer's bankroll: {player.bankroll} chips\n")
                        dealer_turn = False
                        game_on = False
                        break
                    elif bust(dealer):
                        print(f"\nIt's a BUST, Player {player.name} wins!")
                        player.bankroll += bet * 2
                        print(f"{player.name}'s bankroll: {player.bankroll} chips\n")
                        dealer_turn = False
                        game_on = False
                        break
                    else:
                        continue
                if dealer_under21 == True and dealer_turn == True:
                    print("\nDealer wins!")
                    dealer.bankroll += bet
                    player.bankroll -= bet
                    print(
                        f"Casino received {bet} chips\n{player.name}'s bankroll: {player.bankroll} chips\n")
                    dealer_turn = False
                    game_on = False
                    break
                elif dealer_under21 == False and dealer_turn == True:
                    print(f"\nIt's a BUST, Player {player.name} wins!")
                    player.bankroll += bet * 2
                    print(f"{player.name}'s bankroll: {player.bankroll} chips\n")
                    dealer_turn = False
                    game_on = False
                    break
    replay()


"""
Asks the player to replay.
"""


def replay():
    answer = 'wrong'
    while answer not in ['yes', 'no']:
        answer = input("Would you like to play again? Yes or No? ").lower()
    if answer == 'yes':
        game()
    else:
        print("See you next time!")


"""
Introduces the game, asks for the player's username and bankroll.
"""
print("="*60)
print("""Welcome to Blackjack in Python!
      \nShuffle up and deal — the cards are ready!
      \nPlace your bet, watch the dealer’s hidden card, and decide:
      \nwill you Hit for more or Stand with what you’ve got?
      \nTry to beat the dealer without going over 21, and see how long your chips last.
      \nReady to play?\n'Yes' or 'No': """, end='')
yes_or_no = 'wrong'
while yes_or_no not in ['yes', 'no']:
    yes_or_no = input("").lower()

    if yes_or_no not in ['yes', 'no']:
        print("Not a valid answer! Write again: ", end="")
if yes_or_no == 'yes':
    valid_name = False

    while valid_name == False:
        try:
            name = input("How would you like to be called? ")
        except:
            print("Invalid name!")
        else:
            valid_name = True

    valid_bankroll = False

    while valid_bankroll == False:
        try:
            bankroll = int(input("What's your bankroll?\n1 chip = $1: "))
        except:
            print("Invalid bankroll!")
        else:
            valid_bankroll = True

    player = Player(name, bankroll)
    dealer = Dealer("Dealer")
    game()
else:
    print("See you next time!")
