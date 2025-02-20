class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
    
    def getValue(self):
        total = 0
        aces = 0

        for card in self.cards:
            if card.name in ["J", "Q", "K"]:
                total += 10
            elif card.name == "A":
                total += 11
                aces += 1
            else:
                total += int(card.name)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)