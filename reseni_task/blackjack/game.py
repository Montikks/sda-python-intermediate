from deck import Deck
from player import Player, Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def deal_cards(self):
        for player in self.players + [self.dealer]:
            player.add_card(self.deck.deal_card())
            player.add_card(self.deck.deal_card())

    def collect_bets(self):
        for player in self.players:
            while True:
                try:
                    amount = int(input(f"{player.name}, how much would you like to bet? "))
                    if amount > 0:
                        player.place_bet(amount)
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Please enter a valid number for the bet.")

    def play(self):
        self.deck.shuffle()
        self.deal_cards()
        self.collect_bets()
        for player in self.players:
            while not player.is_busted():
                response = input(f"{player.name}, do you want another card? (yes/no): ").strip().lower()
                if response == 'yes':
                    player.add_card(self.deck.deal_card())
                elif response == 'no':
                    break
                else:
                    print("Please type 'yes' or 'no'.")
        self.dealer.play(self.deck)
        self.evaluate_results()

    def evaluate_results(self):
        dealer_value = self.dealer.get_hand_value()
        dealer_blackjack = dealer_value == 21 and len(self.dealer.hand.cards) == 2
        for player in self.players:
            player_value = player.get_hand_value()
            if dealer_blackjack:
                if player.insurance_bet:
                    player.balance += player.insurance_bet * 3  # Insurance pays 2:1
                    print(f"{player.name} wins insurance.")
                if not player.is_busted() and player_value == 21 and len(player.hand.cards) == 2:
                    print(f"{player.name} has Blackjack but dealer also. Push.")
                else:
                    player.lose_bet()
            else:
                if player.insurance_bet:
                    print(f"{player.name} loses insurance bet.")
                if player.is_busted():
                    player.lose_bet()
                elif player_value > dealer_value or dealer_value > 21:
                    player.win_bet()
                else:
                    player.lose_bet()

    def play(self):
        self.deck.shuffle()
        self.deal_cards()
        self.collect_bets()
        for player in self.players:
            self.player_turn(player)
        self.dealer.play(self.deck)
        self.evaluate_results()

    def player_turn(self, player):
        player.show_hand()
        if len(player.hand.cards) == 2:  # Možnost vzdát se hry je dostupná pouze po rozdání prvních dvou karet
            response = input(f"{player.name}, do you want to surrender? (yes/no): ").strip().lower()
            if response == 'yes':
                if player.surrender():
                    return  # Ukonečit tah hráče po vzdání se
                else:
                    print("Cannot surrender at this moment.")  # V případě, že vzdání není možné

        while not player.is_busted():
            response = input(f"{player.name}, do you want another card? (yes/no): ").strip().lower()
            if response == 'yes':
                player.add_card(self.deck.deal_card())
            elif response == 'no':
                break
            else:
                print("Please type 'yes' or 'no'.")

    def player_turn_after_split(self, original_player, split_hand, split_bet):
        # Handle the turns for each of the split hands separately
        for hand, bet in [(original_player.hand, original_player.bet), (split_hand, split_bet)]:
            while not original_player.is_busted():
                print(f"{original_player.name}'s hand with bet {bet}: {hand}")
                if input("Do you want another card? (yes/no): ").strip().lower() == 'yes':
                    hand.add_card(self.deck.deal_card())
                    if original_player.is_busted():
                        print(f"{original_player.name} is busted with hand {hand}.")
                        break

    def offer_insurance(self):
        if self.dealer.hand.cards[0].value == 'A':
            for player in self.players:
                print(f"Dealer's first card is an Ace.")
                if input(f"{player.name}, would you like to buy insurance? (yes/no): ").strip().lower() == 'yes':
                    insurance_bet = player.bet / 2
                    if player.balance >= insurance_bet:
                        player.balance -= insurance_bet
                        player.insurance_bet = insurance_bet
                        print(f"{player.name} has placed an insurance bet of {insurance_bet}.")
                    else:
                        print(f"{player.name} does not have enough balance for insurance.")
                else:
                    player.insurance_bet = 0


if __name__ == "__main__":
    game = Game()
    game.add_player("Alice")
    game.add_player("Bob")
    game.play()
