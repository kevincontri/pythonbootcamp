import random

# Outside variables storing immutable data as tuples
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Creates a card, with a suit, rank and values


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Instantiate a new deck:
#     Create all 52 Card objects; Hold them as a list;
# Shuffle a Deck through a method call:
#     Random library shuffle() function
# Deal card from the Deck object:
#    Pop method from cards list
# Deck Class will return Card class object instances, not just normal python data types


class Deck:

    def __init__(self):

        # List holding all 52 cards
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
        print("Deck shuffled!")

    def deal_one(self):
        return self.all_cards.pop()

# Player class:
#    This class will be used to hold a player's current list of cards
#    A player should be able to add or remove cards from their "hand", or list of Card objects.
#    Must be able to add a single card or multiple cards to their list.
#    Translating a deck/hand of cards with a top and bottom, to a python list.


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # multiple cards objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # single card object
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


def game():
    player1 = Player("One")
    player2 = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player1.add_cards(new_deck.deal_one())
        player2.add_cards(new_deck.deal_one())

    print(f"{player1} and {player2}!")

    game_on = True

    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round {round_num}")

        # check if anyone lost
        if len(player1.all_cards) == 0:
            print("Player One is out of cards! Player Two Wins!")
            game_on = False
            break

        if len(player2.all_cards) == 0:
            print("Player Two, out of cards! Player One Wins!")
            game_on = False
            break

        # Start new round

        player_one_cards = [] # This list simulates current cards on table
        player_one_cards.append(player1.remove_one())

        player_two_cards = []
        player_two_cards.append(player2.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:
                player1.add_cards(player_one_cards)
                player1.add_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player2.add_cards(player_two_cards)
                player2.add_cards(player_one_cards)

                at_war = False

            else:
                print("War!")
                if len(player1.all_cards) < 5:
                    print("Player One Unable To Declare War!")
                    print("Player Two Wins!")
                    game_on = False
                    break

                elif len(player2.all_cards) < 5:
                    print("Player Two Unable To Declare War!")
                    print("Player One Wins!")
                    game_on = False
                    break

                else:
                    for num in range(5):
                        player_one_cards.append(player1.remove_one())
                        player_two_cards.append(player2.remove_one())


game()
