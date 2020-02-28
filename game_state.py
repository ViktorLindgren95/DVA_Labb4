class game_state:
    def __init__(self, player, game_board):
        self.player_num = player
        self.board = game_board
        self.legal_moves = []
        self.extra_turn=False

    def calc_legal(self):
        legal_moves = []
        if self.player_num == 1:
            for i in range(6):
                if self.board[i] > 0:
                    self.legal_moves.append(i)
        else:
            for i in range(7, 13):
                if self.board[i] > 0:
                    self.legal_moves.append(i)

    def move(self, chosen):
        num_balls = self.board[chosen]
        #print(num_balls)
        pit = chosen + 1
        self.board[chosen]=0
        for i in range(num_balls):
            if pit > 13 or pit == 13 and self.player_num == 1:
                pit = 0
            if pit == 6 and self.player_num == 2:
                pit += 1
            self.board[pit] += 1
            pit+=1
        pit=pit-1
        if pit==6 and self.player_num==1 or pit==13 and self.player_num==2:
            self.extra_turn=True
        else:
            self.extra_turn=False
        return game_state(self.player_num,self.board)

    def utility(self):
        util_score=0
        if self.player_num==1:
            util_score=self.board[6]-self.board[13]
        else:
            util_score=self.board[13]-self.board[6]
        return util_score