from basic_graphics import Window, Cell, Line, Point
from time import sleep

class Maze:
    def __init__(
            self, 
            x1: int, 
            y1: int, 
            num_rows: int, 
            num_cols: int, 
            cell_size_x: int, 
            cell_size_y:int , 
            win: Window) -> None:
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
        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)

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
        self._win.redraw()
        sleep(0.05)