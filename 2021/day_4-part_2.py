class BingoBoard():
    def __init__(self):
        self.board = []
        self.has_won = False
        self.last_call = None

    def create(self, board:list[str]) -> None:
        temp = []
        for line in board:
            row = []
            for j in range(0,14,3):
                row.append(line[j:j+2])
            temp.append(row)
        self.board = [[item.strip() for item in row] for row in temp]

    def display(self) -> None:
        for row in self.board:
            for item in row:
                if len(item) == 2:
                    print(item, end=' ')
                elif len(item) == 1:
                    print(' ' + item, end=' ')
                else:
                    print(' x', end=' ')
            print()
        print()

    def call(self, called_number:str) -> None:
        self.last_call = int(called_number)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == called_number:
                    self.board[i][j] = ''

    def has_bingo(self) -> bool:
        for row in self.board:
            if ''.join(row) == '':
                self.has_won = True
                return True
        for row in [list(x) for x in zip(*self.board)]:
            if ''.join(row) == '':
                self.has_won = True
                return True
        return False

    def score_board(self) -> int:
        score = 0
        for row in self.board:
            for number in row:
                score += int(number if number != '' else 0)
        score *= self.last_call
        return score


if __name__ == '__main__':
    bingo_boards = []
    bingo_calls = []
    with open('day_4-input') as f:
        bingo_calls = [number.rstrip() for number in f.readline().split(',')]
        f.readline()

        while True:
            bingo_boards.append(BingoBoard())
            bingo_boards[-1].create([f.readline().rstrip() for i in range(5)])
            if f.readline() == '':
                break

    for call in bingo_calls:
        for board in bingo_boards:
            if not board.has_won:
                board.call(call)
                board.has_bingo()
        if all([board.has_won for board in bingo_boards]):
            break

    winning_board = [board for board in bingo_boards if int(board.last_call) == int(call)][0]
    winning_board.display()
    print(winning_board.score_board())
