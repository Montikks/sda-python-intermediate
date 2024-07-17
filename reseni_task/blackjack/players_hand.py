class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                ace_count += 1
                value += 11
            else:
                value += int(card.value)
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def is_busted(self):
        return self.get_value() > 21

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = Hand()
        self.bet = 0  # Přidání atributu sázky

    def add_card(self, card):
        self.hand.add_card(card)

    def place_bet(self, amount):
        if amount <= self.balance:
            self.bet = amount
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def win_bet(self):
        self.balance += self.bet * 2
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer", float('inf'))
