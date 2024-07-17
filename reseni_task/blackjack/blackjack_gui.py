import tkinter as tk
from PIL import Image, ImageTk
import os
from cards_deck import Deck, load_card_images
from players_hand import Player, Dealer


class BlackjackGUI:
	def __init__(self, master):
		self.master = master
		self.master.title("Blackjack")

		# Nastavení pozadí (volitelné)
		if os.path.exists("images/background.png"):
			self.background_image = Image.open("images/background.png")
			self.background_photo = ImageTk.PhotoImage(self.background_image)
			self.background_label = tk.Label(master, image=self.background_photo)
			self.background_label.place(relwidth=1, relheight=1)

		# Přidání loga (volitelné)
		if os.path.exists("images/logo.png"):
			self.logo_image = Image.open("images/logo.png")
			self.logo_photo = ImageTk.PhotoImage(self.logo_image)
			self.logo_label = tk.Label(master, image=self.logo_photo)
			self.logo_label.pack()

		self.card_images = load_card_images('cards')

		self.status_label = tk.Label(master, text="Welcome to Blackjack", height=4)
		self.status_label.pack()

		self.player_frame = tk.Frame(master)
		self.player_frame.pack(side=tk.LEFT, padx=20)

		self.dealer_frame = tk.Frame(master)
		self.dealer_frame.pack(side=tk.RIGHT, padx=20)

		self.player_label = tk.Label(master, text="Player", font=("Helvetica", 16))
		self.player_label.pack(in_=self.player_frame, side=tk.TOP)

		self.dealer_label = tk.Label(master, text="Dealer", font=("Helvetica", 16))
		self.dealer_label.pack(in_=self.dealer_frame, side=tk.TOP)

		self.hit_button = tk.Button(master, text="Hit", command=self.hit)
		self.hit_button.pack(side=tk.LEFT)

		self.stand_button = tk.Button(master, text="Stand", command=self.stand)
		self.stand_button.pack(side=tk.LEFT)

		self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
		self.reset_button.pack(side=tk.LEFT)

		self.reset_game()

	def reset_game(self):
		self.deck = Deck()
		self.player = Player("Player 1", 1000)
		self.dealer = Dealer()

		for widget in self.player_frame.winfo_children():
			widget.destroy()
		for widget in self.dealer_frame.winfo_children():
			widget.destroy()

		self.status_label.config(text="Welcome to Blackjack")
		self.hit_button.config(state=tk.NORMAL)
		self.stand_button.config(state=tk.NORMAL)

		self.player_label.pack(in_=self.player_frame, side=tk.TOP)
		self.dealer_label.pack(in_=self.dealer_frame, side=tk.TOP)

		self.player.add_card(self.deck.deal_card())
		self.player.add_card(self.deck.deal_card())
		self.dealer.add_card(self.deck.deal_card())
		self.dealer.add_card(self.deck.deal_card())

		self.show_initial_cards()

	def show_initial_cards(self):
		for card in self.player.hand.cards:
			self.show_card(self.player_frame, card)
		self.show_card(self.dealer_frame, self.dealer.hand.cards[0])

	def hit(self):
		card = self.deck.deal_card()
		self.player.add_card(card)
		self.show_card(self.player_frame, card)
		if self.player.hand.is_busted():
			self.status_label.config(text=f"{self.player.name} is busted! Dealer wins.")
			self.hit_button.config(state=tk.DISABLED)
			self.stand_button.config(state=tk.DISABLED)

	def stand(self):
		self.hit_button.config(state=tk.DISABLED)
		self.stand_button.config(state=tk.DISABLED)
		self.dealer_play()

	def show_card(self, frame, card):
		value = card.value
		if card.value.isdigit() and int(card.value) < 10:
			value = f'0{card.value}'
		key = f'{value}{card.suit[0].upper()}'
		card_image = self.card_images[key]
		label = tk.Label(frame, image=card_image)
		label.image = card_image
		label.pack()

	def dealer_play(self):
		while self.dealer.hand.get_value() < 17:
			card = self.deck.deal_card()
			self.dealer.add_card(card)
			self.show_card(self.dealer_frame, card)
		self.evaluate_results()

	def evaluate_results(self):
		dealer_value = self.dealer.hand.get_value()
		player_value = self.player.hand.get_value()
		if self.player.hand.is_busted() or (dealer_value <= 21 and player_value < dealer_value):
			self.status_label.config(text=f"{self.player.name} loses.")
		elif dealer_value > 21 or player_value > dealer_value:
			self.status_label.config(text=f"{self.player.name} wins!")
		else:
			self.status_label.config(text="It's a tie!")


if __name__ == "__main__":
	root = tk.Tk()
	app = BlackjackGUI(root)
	root.mainloop()
