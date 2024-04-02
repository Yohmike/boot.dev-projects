from basic_graphics import Window, Cell, Line, Point
from time import sleep

import random


class Maze:
    def __init__(
            self, 
            x1: int, 
            y1: int, 
            num_rows: int, 
            num_cols: int, 
            cell_size_x: int, 
            cell_size_y:int , 
            win: Window = None,
            seed = None) -> None:
        if seed is not None:
            random.seed(seed)
        self.corner = Point(x1, y1)
        self.rows = num_rows
        self.cols = num_cols
        self.cell_x = cell_size_x
        self.cell_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self.cols):
            cells = []
            for j in range(self.rows):
                cell = self.__make_cell(i, j)
                cells.append(cell)
            self._cells.append(cells)
        for i in range(self.rows):
            for j in range(self.cols):
                self._draw_cell(j, i)

    def __make_cell(self, i, j) -> Cell:
        x1 = self.corner.x + i * self.cell_x
        y1 = self.corner.y + j * self.cell_y
        x2 = x1 + self.cell_x
        y2 = y1 + self.cell_y
        top_left = Point(x1, y1)
        bottom_right = Point(x2, y2)
        return Cell(
            bottom_right=bottom_right, 
            top_left=top_left, 
            window=self._win
        )

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self.cols - 1, self.rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            dir = ""
            if i > 1 and not self._cells[i-1][j].visited:
                dir += "W"
                to_visit.append((i - 1, j))
            if i < self.cols - 1 and not self._cells[i+1][j].visited:
                dir += "E"
                to_visit.append((i + 1, j))
            if j > 1 and not self._cells[i][j - 1].visited:
                dir += "N"
                to_visit.append((i, j - 1))
            if j < self.rows - 1 and not self._cells[i][j + 1].visited:
                dir += "S"
                to_visit.append((i, j + 1))
            if dir == "":
                self._cells[i][j].draw()
                return
            else:
                direction = random.randrange(0, len(dir))
                # print(i, j, dir, direction)
                self._break_wall(i, j, dir[direction])
                self._break_walls_r(*to_visit[direction])

    def _break_wall(self, i, j, direction):
        if direction == "N":
            self._cells[i][j].has_top_wall = False
            self._cells[i][j - 1].has_bottom_wall = False
        if direction == "S":
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j + 1].has_top_wall = False
        if direction == "E":
            self._cells[i][j].has_right_wall = False
            self._cells[i + 1][j].has_left_wall = False
        if direction == "W":
            self._cells[i][j].has_left_wall = False
            self._cells[i - 1][j].has_right_wall = False


    def _reset_cells_visited(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self._cells[i][j].visited = False