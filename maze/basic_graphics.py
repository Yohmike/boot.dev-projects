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