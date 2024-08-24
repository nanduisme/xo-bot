class Game:
    def __init__(self):
        self.board = [None * 9]
        self.is_p1_turn = False

    def play(self, idx):
        if self.board[idx] is not None:
            raise Exception(f"Box {idx} is taken")
    
        self.board[idx] = int(self.is_p1_turn)
        self.is_p1_turn = not self.is_p1_turn

    def is_win(self):
        ...