from maze_solver import Maze_solver

mapa =  [['S', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], [' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], [' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', ' ', ' ', ' ', ' ', ' ', 'E']]
Maze = Maze_solver(mapa)
Maze.solve()
print(Maze)
Maze.shortest_path()

