with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]


class LottoCard:
    def __init__(self, card: str):
        self.card_id = 0
        self.winning_numbers = []
        self.numbers = []
        self.matches = 0
        self.point_value = 0
        self.populate(card)

    def populate(self, card: str):
        self.card_id = int(card.split(':')[0][5:])
        self.winning_numbers = [int(num) for num in card.split(':')[1].split('|')[0].split()]
        self.numbers = [int(num) for num in card.split(':')[1].split('|')[1].split()]
        for number in self.numbers:
            if number in self.winning_numbers:
                self.matches += 1
        if self.matches > 0:
            self.point_value = 2 ** (self.matches - 1)

cards = []
for line in puzzle_input:
    cards.append(LottoCard(line).point_value)
print(cards)
print(sum(cards))
