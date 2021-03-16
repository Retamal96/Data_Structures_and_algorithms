
"""
We need to find a position in a chess board where N queens are in the board, but any of them 
threaten each other

The problem is solved, if you can place all the queens.
if one queen cant be place, you lose

1- First, draw the board
2- One aproach could be, starting in a1(0,0) and placing there the 1 queen,
   then, checking the squares covered by the first queen, find one to place the second queen
3- to sve time, we know there cant be a queen in the same column or row, qe can skip that and
   only check the diagonal.
4- we will use backtracking to check all the options
"""


class Nqueens():

    def __init__(self):
        self.board = []
        for row in range(8):
            self.board.append([])
            for column in range(8):
                self.board[row].append(' ')

        self.numbers_of_queens_on_board = 0       
        self.is_solve = False


    def solve(self):
        #print(self)
        if self.numbers_of_queens_on_board == 8:
            self.is_solve = True
            print(self)
        if not self.is_solve:
            for row in range(8):
                if self._can_put_queen(row):
                    self.board[row][self.numbers_of_queens_on_board] = 'Q' #this works bc we dont need to check columns where we alredy place one Q
                    self.numbers_of_queens_on_board += 1
                    self.solve()
                    self.numbers_of_queens_on_board -= 1
                    self.board[row][self.numbers_of_queens_on_board] = ' ' #this works bc we dont need to check columns where we alredy place one Q                


    def _can_put_queen(self, row):
        return self._row_is_clear(row) and \
            self._diagonal_up_is_clear(row) and \
            self._diagonal_down_is_clear(row)

    def _row_is_clear(self, row):
        return 'Q' not in self.board[row]
    

    """
    We are only checking the parts were we already place a queen, since its impossible to have a Q further
    """
    def _diagonal_up_is_clear(self, row):
        current_row = row -1
        current_column = self.numbers_of_queens_on_board - 1

        while current_column >= 0 and current_row >= 0:
            if self.board[current_row][current_column] == 'Q': #Remeber we can only place Q in unique columns
                return False
            current_column -= 1
            current_row -=1
            
        return True

    def _diagonal_down_is_clear(self, row):
        current_row= row +1
        current_column = self.numbers_of_queens_on_board - 1 

        while current_column >=0 and current_row < len(self.board):
            if self.board[current_row][current_column] =='Q':
                return False
            current_row += 1 
            current_column -= 1
        return True



    def __str__(self):
        result = ""
        for row in self.board:
            result += str(row) + '\n'
        return result