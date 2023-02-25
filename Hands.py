class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        had_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                had_ace = True
        if had_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        if self.dealer:
            print("Dealer's hand: ")
        else:
            print("Your hand: ")
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards and not self.is_blackjack():
                print('┌───────┐')
                print('|   h   |')
                print('|   i   |')
                print('|   d   |')
                print('|   d   |')
                print('|   e   |')
                print('|   n   |')
                print('└───────┘')
            else:
                if card.rank["rank"] == "10":
                    print('┌───────┐')
                    print(f'|{card.rank["rank"]}     |')
                    print('|       |')
                    print(f'|   {card.suits}   |')
                    print('|       |')
                    print(f'|     {card.rank["rank"]}|')
                    print('└───────┘')
                else:
                    print('┌───────┐')
                    print(f'|{card.rank["rank"]}      |')
                    print('|       |')
                    print(f'|   {card.suits}   |')
                    print('|       |')
                    print(f'|     {card.rank["rank"]} |')
                    print('└───────┘')
                # print(card)
            # if not self.dealer:
            #    print("Value:", self.get_value())
        print()

