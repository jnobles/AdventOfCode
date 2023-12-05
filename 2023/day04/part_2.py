with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]


class LottoCard:
    def __init__(self, card: str):
        self.card_id = 0
        self.winning_numbers = []
        self.numbers = []
        self.matches = 0
        self.populate(card)

    def populate(self, card: str):
        self.card_id = int(card.split(':')[0][5:])
        self.winning_numbers = [int(num) for num in card.split(':')[1].split('|')[0].split()]
        self.numbers = [int(num) for num in card.split(':')[1].split('|')[1].split()]
        for number in self.numbers:
            if number in self.winning_numbers:
                self.matches += 1

    def __str__(self):
        return f'Card {self.card_id}: {self.matches} matches'

cards = []
card_ref = []
for line in puzzle_input:
    cards.append(LottoCard(line))
    card_ref.append(LottoCard(line))
card_index = 0
while card_index < len(cards):
    if cards[card_index].matches > 0:
        #cards_to_copy = range(cards[card_index].card_id + 1, cards[card_index].card_id + 1 + cards[card_index].matches)
        #for i in cards_to_copy:
        cards[card_index + 1:card_index + 1] = card_ref[cards[card_index].card_id:cards[card_index].card_id + cards[card_index].matches]
    card_index += 1

print(len(cards))