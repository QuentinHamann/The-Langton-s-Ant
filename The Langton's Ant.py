board = []

class ant :
    def __init__(self):
        self.antx = 5
        self.anty = 5
        self.col = 10
        self.row=10
        self.direction = 0
        
        #N = 0
        #E = 1
        #S = 2
        #O = 3
    
    def board(self):
        board = [[0] * self.col for i in range(self.row)]
        for i in range (self.row):
            for j in range (self.col):
                board[i][j] = 0
        board[self.antx][self.anty] = "test"
        for row in board :
            print (' '.join([str(elem)for elem in row]))
        print(' ')

    def antmove (self):
        #case blanche
        if board[self.antx][self.anty]== 0:
            self.direction = self.direction+1
            if self.direction == 4:
                self.direction= 0
            else :
                self.direction = self.direction
            
            if self.direction == 0:
                board[self.antx][self.anty]==1
                board[self.antx][self.anty+1]==0
            elif self.direction == 1:
                board[self.antx][self.anty]==1
                board[self.antx+1][self.anty]==0
            elif self.direction == 2:
                board[self.antx][self.anty]==1
                board[self.antx][self.anty-1]==0
            elif self.direction == 3:
                board[self.antx][self.anty]==1
                board[self.antx-1][self.anty]==0
        #Case Noire
        if board[self.antx][self.anty] ==1:
            self.direction = self.direction-1
            if self.direction == -1:
                self.direction= 3
            else :
                self.direction = self.direction
            
            if self.direction == 0:
                board[self.antx][self.anty]==0
                board[self.antx][self.anty+1]==1
            elif self.direction == 1:
                board[self.antx][self.anty]==0
                board[self.antx+1][self.anty]==1
            elif self.direction == 2:
                board[self.antx][self.anty]==0
                board[self.antx][self.anty-1]==1
            elif self.direction == 3:
                board[self.antx][self.anty]==0
                board[self.antx-1][self.anty]==1

obj= ant()
obj.board()