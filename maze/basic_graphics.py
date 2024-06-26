from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Test"
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: 'Line', fill_color: str):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def __repr__(self) -> str:
        return f"Point({self.__x}, {self.__y})"

class Line:
    def __init__(self, from_point: Point , to_point: Point) -> None:
        self.__from = from_point
        self.__to = to_point

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__from.x, self.__from.y, 
            self.__to.x, self.__to.y, 
            fill=fill_color, 
            width=2
        )
        canvas.pack(fill=BOTH, expand=1)

    def __repr__(self) -> str:
        return f"Line( from {self.__from} to {self.__to})"


class Cell:
    def __init__(self, bottom_right: Point, top_left: Point, window: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1, self._y1 = top_left.x, top_left.y
        self._x2, self._y2 = bottom_right.x, bottom_right.y
        self._win = window
        self.visited = False

    def draw(self, fill_color: str = "black") -> None:
        if self._win is None:
            return
        top_right = Point(self._x2, self._y1)
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)
        left_line = Line(from_point=top_left, to_point=bottom_left)
        right_line = Line(from_point=top_right, to_point=bottom_right)
        top_line = Line(from_point=top_left, to_point=top_right)
        bottom_line = Line(from_point=bottom_left, to_point=bottom_right)
        default_color = "#d9d9d9"
        if self.has_left_wall:
            self._win.draw_line(left_line, fill_color=fill_color)
        else:
            self._win.draw_line(left_line, fill_color=default_color)
        if self.has_right_wall:
            self._win.draw_line(right_line, fill_color=fill_color)
        else:
            self._win.draw_line(right_line, fill_color=default_color)
        if self.has_top_wall:
            self._win.draw_line(top_line, fill_color=fill_color)
        else:
            self._win.draw_line(top_line, fill_color=default_color)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, fill_color=fill_color)
        else:
            self._win.draw_line(bottom_line, fill_color=default_color)
    
    def add_walls(self, walls: str) -> None:
        if "N" not in walls:
            self.has_top_wall = False
        if "E" not in walls:
            self.has_right_wall = False
        if "S" not in walls:
            self.has_bottom_wall = False
        if "W" not in walls:
            self.has_left_wall = False
    
    def get_center(self):
        if self._x1 == self._x2 == 0:
            x = 0
        elif self._x1 > self._x2:
            x = self._x1 - (self._x1 - self._x2) / 2
        elif self._x1 <= self._x2:
            x = self._x2 - (self._x2 - self._x1) / 2
        
        if self._y1 == self._y2 == 0:
            y = 0
        elif self._y1 > self._y2:
            y = self._y1 - (self._y1 - self._y2) / 2
        elif self._y1 <= self._y2:
            y = self._y2 - (self._y2 - self._y1) / 2
        
        return Point(x, y)

    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"
        center1 = self.get_center()
        center2 = to_cell.get_center()

        self._win.draw_line(Line(center1, center2), color)