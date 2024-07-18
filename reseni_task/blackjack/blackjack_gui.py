import tkinter as tk
from PIL import Image, ImageTk
import os
from cards_deck import Deck, load_card_images
from players_hand import Player, Dealer, Hand

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

        self.balance_label = tk.Label(master, text="Balance: $1000", font=("Helvetica", 16))
        self.balance_label.pack()

        self.bet_label = tk.Label(master, text="Enter your bet:", font=("Helvetica", 16))
        self.bet_label.pack()

        self.bet_entry = tk.Entry(master)
        self.bet_entry.pack()

        self.place_bet_button = tk.Button(master, text="Place Bet", command=self.place_bet)
        self.place_bet_button.pack()

        self.insurance_button = tk.Button(master, text="Insurance", command=self.insurance, state=tk.DISABLED)
        self.insurance_button.pack()

        self.double_down_button = tk.Button(master, text="Double Down", command=self.double_down, state=tk.DISABLED)
        self.double_down_button.pack()

        self.split_button = tk.Button(master, text="Split", command=self.split, state=tk.DISABLED)
        self.split_button.pack()

        self.player_frame = tk.Frame(master)
        self.player_frame.pack(side=tk.LEFT, padx=20)

        self.dealer_frame = tk.Frame(master)
        self.dealer_frame.pack(side=tk.RIGHT, padx=20)

        self.player_label = tk.Label(master, text="Player", font=("Helvetica", 16))
        self.player_label.pack(in_=self.player_frame, side=tk.TOP)

        self.dealer_label = tk.Label(master, text="Dealer", font=("Helvetica", 16))
        self.dealer_label.pack(in_=self.dealer_frame, side=tk.TOP)

        self.hit_button = tk.Button(master, text="Hit", command=self.hit, state=tk.DISABLED)
        self.hit_button.pack(side=tk.LEFT)

        self.stand_button = tk.Button(master, text="Stand", command=self.stand, state=tk.DISABLED)
        self.stand_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT)

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game, state=tk.DISABLED)
        self.new_game_button.pack(side=tk.LEFT)

        self.player_balance = 1000  # Uchováváme zůstatek hráče
        self.reset_game(initial=True)

    def place_bet(self):
        try:
            bet_amount = int(self.bet_entry.get())
            self.player.place_bet(bet_amount)
            self.balance_label.config(text=f"Balance: ${self.player.balance}")
            self.status_label.config(text=f"Bet placed: ${bet_amount}")
            self.hit_button.config(state=tk.NORMAL)
            self.stand_button.config(state=tk.NORMAL)
            self.place_bet_button.config(state=tk.DISABLED)
            self.bet_entry.config(state=tk.DISABLED)

            # Umožnit pojištění, pokud dealerova karta je eso
            if self.dealer.hand.cards[0].value == 'A':
                self.insurance_button.config(state=tk.NORMAL)
            else:
                self.insurance_button.config(state=tk.DISABLED)

            # Umožnit zdvojnásobení sázky a rozdělení ruky
            self.double_down_button.config(state=tk.NORMAL)
            if self.player.hand.cards[0].value == self.player.hand.cards[1].value:
                self.split_button.config(state=tk.NORMAL)
            else:
                self.split_button.config(state=tk.DISABLED)

        except ValueError:
            self.status_label.config(text="Invalid bet amount. Please enter a valid number.")

    def insurance(self):
        insurance_amount = self.player.bet / 2
        if insurance_amount <= self.player.balance:
            self.player.balance -= insurance_amount
            self.balance_label.config(text=f"Balance: ${self.player.balance}")
            self.status_label.config(text=f"Insurance placed: ${insurance_amount}")
            if self.dealer.hand.get_value() == 21:
                self.player.balance += self.player.bet
                self.status_label.config(text=f"Dealer has Blackjack! Insurance wins.")
            else:
                self.status_label.config(text=f"Dealer does not have Blackjack. Insurance lost.")
        else:
            self.status_label.config(text="Insufficient balance for insurance.")
        self.insurance_button.config(state=tk.DISABLED)

    def double_down(self):
        if self.player.bet * 2 <= self.player.balance:
            self.player.place_bet(self.player.bet)
            self.balance_label.config(text=f"Balance: ${self.player.balance}")
            self.status_label.config(text=f"Bet doubled to: ${self.player.bet * 2}")
            self.hit()
            self.stand()
        else:
            self.status_label.config(text="Insufficient balance for doubling down.")
        self.double_down_button.config(state=tk.DISABLED)
        self.split_button.config(state=tk.DISABLED)

    def split(self):
        if self.player.balance < self.player.bet:
            self.status_label.config(text="Insufficient balance to split.")
            return

        self.split_hand = Hand()
        self.split_hand.add_card(self.player.hand.cards.pop())
        self.player.place_bet(self.player.bet)

        self.balance_label.config(text=f"Balance: ${self.player.balance}")
        self.status_label.config(text="Hand split. Playing first hand.")

        self.show_initial_cards()
        self.split_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)

    def reset_game(self, initial=False):
        if not initial:
            self.player_balance = self.player.balance

        self.deck = Deck()
        self.player = Player("Player 1", self.player_balance)
        self.dealer = Dealer()
        self.split_hand = None

        for widget in self.player_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        self.status_label.config(text="Welcome to Blackjack")
        self.balance_label.config(text=f"Balance: ${self.player.balance}")
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.place_bet_button.config(state=tk.NORMAL)
        self.bet_entry.config(state=tk.NORMAL)
        self.bet_entry.delete(0, tk.END)
        self.insurance_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)
        self.split_button.config(state=tk.DISABLED)

        self.player_label.pack(in_=self.player_frame, side=tk.TOP)
        self.dealer_label.pack(in_=self.dealer_frame, side=tk.TOP)

        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        self.show_initial_cards()

    def new_game(self):
        self.player_balance = 1000
        self.reset_game(initial=True)
        self.new_game_button.config(state=tk.DISABLED)

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
            self.double_down_button.config(state=tk.DISABLED)
            self.split_button.config(state=tk.DISABLED)
            if self.player.balance == 0:
                self.status_label.config(text="Game Over. You have no more balance.")
                self.new_game_button.config(state=tk.NORMAL)

    def stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_down_button.config(state=tk.DISABLED)
        self.split_button.config(state=tk.DISABLED)
        if self.split_hand:
            self.player.hand = self.split_hand
            self.split_hand = None
            self.status_label.config(text="Playing split hand.")
            self.hit_button.config(state=tk.NORMAL)
            self.stand_button.config(state=tk.NORMAL)
        else:
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

        print(f"Dealer's final hand: {self.dealer.hand} => Total value: {dealer_value}")
        print(f"{self.player.name}'s final hand: {self.player.hand} => Total value: {player_value}")

        if self.player.hand.is_busted():
            self.status_label.config(text=f"{self.player.name} is busted! Dealer wins.")
            self.player.lose_bet()
        elif self.dealer.hand.is_busted():
            self.status_label.config(text=f"Dealer is busted! {self.player.name} wins!")
            self.player.win_bet()
        elif player_value > dealer_value:
            self.status_label.config(text=f"{self.player.name} wins!")
            self.player.win_bet()
        elif player_value < dealer_value:
            self.status_label.config(text=f"Dealer wins.")
            self.player.lose_bet()
        else:
            self.status_label.config(text="It's a tie!")
            self.player.push()

        self.balance_label.config(text=f"Balance: ${self.player.balance}")

        if self.player.balance == 0:
            self.status_label.config(text="Game Over. You have no more balance.")
            self.new_game_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
