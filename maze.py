from window import *
from cell import *
import time
import random

class Maze(object):
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):

        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited() # reset status so we can use it in solving the maze


    def _create_cells(self):

        for row in range(self.num_rows):
            single_row_list = []

            for col in range(self.num_cols):
                single_row_list.append(Cell(win=self._win))

            self._cells.append(single_row_list)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)
                


    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1 = self._x1 + j * (self._cell_size_x)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + i * (self._cell_size_y)
        y2 = y1 + self._cell_size_y
            
        self._cells[i][j].draw(x1,x2,y1,y2)

        self._animate()
        # gets position of cell within maze

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = 0
        self._draw_cell(0,0)

        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = 0
        self._draw_cell(self.num_rows - 1,self.num_cols - 1)

    def _break_walls_r(self,i,j):
        self._cells[i][j]._visited = True

        # print('started')
        while True:
            to_visit = []
            
            # print(self._cells[i-1][j]._visited,self._cells[i+1][j]._visited,
                #   self._cells[i][j-1]._visited,self._cells[i][j+1]._visited)

            if i > 0 and self._cells[i-1][j]._visited == False:
                to_visit.append((i-1,j))
                # print('top appended')

            if j > 0 and self._cells[i][j-1]._visited == False:
                to_visit.append((i,j-1))
                # print('left appended')

            if i < self.num_rows - 1 and self._cells[i+1][j]._visited == False:
                to_visit.append((i+1,j))
                # print('bottom appended')

            if j < self.num_cols - 1 and self._cells[i][j+1]._visited == False:
                to_visit.append((i,j+1))
                # print('right appended')

            # print(f"After setting _visited: {self._cells[i][j]._visited}")

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                # print('drawing')
                return
            
            next_cell = random.choice(to_visit)

            if next_cell == (i,j-1):
                self._cells[i][j].has_left_wall = False
                self._cells[i][j-1].has_right_wall = False

            if next_cell == (i,j+1):
                self._cells[i][j].has_right_wall = False
                self._cells[i][j+1].has_left_wall = False

            if next_cell == (i-1,j):
                self._cells[i][j].has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False

            if next_cell == (i+1,j):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False

            # print('wall_broken')
            self._break_walls_r(next_cell[0],next_cell[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j]._visited = True
        if (i,j) == (self.num_rows-1,self.num_cols-1):
            return True
        
        if i > 0 and self._cells[i-1][j]._visited == False and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            res = self._solve_r(i-1,j)
            if res:
                return True
            self._cells[i-1][j].draw_move(self._cells[i][j],undo=True) #gray
            

        if j > 0 and self._cells[i][j-1]._visited == False and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            res = self._solve_r(i,j-1)
            if res:
                return True
            self._cells[i][j-1].draw_move(self._cells[i][j],undo=True) #gray

        if i < self.num_rows - 1 and self._cells[i+1][j]._visited == False and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            res = self._solve_r(i+1,j)
            if res:
                return True
            self._cells[i+1][j].draw_move(self._cells[i][j],undo=True) #gray

        if j < self.num_cols - 1 and self._cells[i][j+1]._visited == False and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            res = self._solve_r(i,j+1)
            if res:
                return True
            self._cells[i][j+1].draw_move(self._cells[i][j],undo=True) #gray

        return False

        