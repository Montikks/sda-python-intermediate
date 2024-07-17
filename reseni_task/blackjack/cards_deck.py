import random
import os
from PIL import Image, ImageTk


class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return f"{self.value} of {self.suit}"


class Deck:
	suits = ['hearts', 'diamonds', 'clubs', 'spades']
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

	def __init__(self):
		self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.cards)

	def deal_card(self):
		return self.cards.pop()


# Načítání obrázků karet
def load_card_images(folder):
	card_images = {}
	suits = ['hearts', 'diamonds', 'clubs', 'spades']
	values = ['A', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K']

	for suit in suits:
		for value in values:
			filename = f"card_{suit}_{value}.png"
			path = os.path.join(folder, filename)
			if os.path.exists(path):
				image = Image.open(path)
				card_images[f'{value}{suit[0].upper()}'] = ImageTk.PhotoImage(image)

	return card_images
