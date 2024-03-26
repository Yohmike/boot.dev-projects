from basic_graphics import Window, Line, Point
def main():
    width = 800
    height = 600
    win = Window(width=width, height=height)

    bottom_left_corner = Point(0, 0)
    bottom_right_corner = Point(width, 0)
    top_left_corner = Point(0, height)
    top_right_corner = Point(width, height)

    win.draw_line(Line(bottom_left_corner, top_right_corner),fill_color="green")
    win.draw_line(Line(top_left_corner, bottom_right_corner),fill_color="red")
    win.wait_for_close()

if __name__ == "__main__":
    main()