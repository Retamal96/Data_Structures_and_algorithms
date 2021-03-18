

class Maze_solver():

    def __init__(self, mapa):
        self.mapa = mapa 
        self.current_position = 'S'
        self.is_solve = False
   
    def solve(self):
        if self.current_position == 'E':
            self.is_solve = True
        
        if not self.is_solve:
            row,column = self.find_start()
            #self.move()
            #self.solve()


    def find_start(self):
        finded = False
        for row in range(len(self.mapa)):
            for column in range(len(self.mapa[row])):
              if self.mapa[row][column] == 'S':
                  finded = True
                  return row,column  
        if finded == False:
            return 'Error'



    def __str__(self):
        result = ""
        for row in self.mapa:
            result += str(row) + '\n'
        return result
