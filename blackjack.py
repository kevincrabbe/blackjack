from random import shuffle

class Card:
	number_face = {11: "jack", 12: "queen", 13: "king"}

	def __init__(self, number, suit):
		self.number = number
		self.suit = suit
		self.has_face = False
		# Try catch block?
		if self.suit == "clubs" or self.suit == "spades":
			self.color = "black"
		elif self.suit == "hearts" or self.suit == "diamonds":
			self. color = "red"
		if number > 10:
			self.face = self.number_face[number]
			self.number = 10
			self.has_face = True

	def __str__(self):
		result = ""
		if self.has_face:
			result += self.face + " "
		else:
			result += str(self.number) + " "
		result += str(self.suit)
		return result

class Deck:
	suit_color = {"clubs": "black", "spades": "black", "hearts": "red", "diamonds": "red"}

	def __init__(self):
		self.cards = list()

		#Used cards pile
		self.used = list()
		for suit in self.suit_color:
			for number in range(1, 14):
				new_card = Card(number, suit)
				self.cards.append(new_card)
		shuffle(self.cards)
	def get_card(self):
		if len(self.cards) == 0:
			self = Deck()
		return self.cards.pop()

class Player:
	amount = 0
	def __init__(self):
		self.hand = list()
	def draw(self, deck):
		self.hand.append(deck.get_card())

def get_value(player):
	# First add all the non ones
	non_ones = [card.number for card in player.hand]
	value = sum(non_ones)
	num_ones = len(player.hand) - len(non_ones)

	# Now add all the ones
	for i in range(num_ones):
		if value + 11 + num_ones - (i + 1) <= 21:
			value += 11
		else:
			value += 1
	return value

def display_hands(player1, player2):
	# Display the hands
	print("Hands:")
	print("----------------")
	print("Player 1 hand: ")
	for card in player1.hand:
		print(card)
	print("Player 2 hand: ")
	for card in player2.hand:
		print(card)


def play_round(player1, player2):
	# find the value of each player's hand

	# Instantiate deck
	deck = Deck()

	# Each player draws two cards
	player1.draw(deck)
	player1.draw(deck)
	player2.draw(deck)
	player2.draw(deck)

	display_hands(player1, player2)

	# Allow users to decide whether or not to hit or stay
	p1_done = False
	p2_done = False
	winner = None
	while(not p1_done or not p2_done):
		print("Player 1, hit or stay (h/s)?: ")
		user_input = input()
		user_input = user_input.upper()
		if user_input == "H":
			player1.draw(deck)
			display_hands(player1, player2)
			print()
			if get_value(player1) > 21:
				return "Player 2"
		else:
			p1_done = True


		print("Player 2, hit or stay (h/s)?: ")
		user_input = input()
		user_input = user_input.upper()
		if user_input == "H":
			player2.draw(deck)
			display_hands(player1, player2)
			print()
			if get_value(player2) > 21:
				return "Player 1"
		else:
			p2_done = True


	# Determine who the winner is
	player1_score = get_value(player1)
	player2_score = get_value(player2)
	if player1_score > player2_score:
		return "Player1"
	elif player2_score > player1_score:
		return "Player2"
	else:
		return "Tie"


# The CLI
game_end = False
while(not game_end):
	print("Press enter to start or q to exit")
	user_input = input()
	user_input = user_input.upper()
	if user_input == "Q":
		break
	player1 = Player()
	player2 = Player()
	print("The winner is " + play_round(player1, player2))
	print("Would you like to play again? (Y/N)")
	user_input = input()
	user_input = user_input.upper()
	if user_input == "N":
		game_end = True
