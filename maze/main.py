from basic_graphics import Window, Line, Point, Cell



def main():
    width = 800
    height = 600
    win = Window(width=width, height=height)

    bottom_left_corner = Point(0, 0)
    bottom_right_corner = Point(width, 0)
    top_left_corner = Point(0, height)
    top_right_corner = Point(width, height)

    # win.draw_line(Line(bottom_left_corner, top_right_corner),fill_color="green")
    # win.draw_line(Line(top_left_corner, bottom_right_corner),fill_color="red")

    w_cell = height / 10 + 1
    h_cell = width / 10 + 1

    cells = [
        (Point(1, 1),Point(w_cell, h_cell), "red", ""),
        (Point(1, 2 * h_cell),Point( w_cell, 3 * h_cell), "green", "N"),
        (Point(1, 4 * h_cell),Point( w_cell, 5 * h_cell), "green", "E"),
        (Point(1, 6 * h_cell),Point( w_cell, 7 * h_cell), "green", "W"),
        (Point(1, 8 * h_cell),Point( w_cell, 9 * h_cell), "green", "S"),
        (Point(2 * w_cell, 1),Point( 3 * w_cell, h_cell), "red", "NE"),
        (Point(2 * w_cell, 2 * h_cell),Point( 3 * w_cell, 3 * h_cell), "red", "ES"),
        (Point(2 * w_cell, 4 * h_cell),Point( 3 * w_cell, 5 * h_cell), "red", "SW"),
        (Point(2 * w_cell, 6 * h_cell),Point( 3 * w_cell, 7 * h_cell), "red", "WN"),
        (Point(2 * w_cell, 8 * h_cell),Point( 3 * w_cell, 9 * h_cell), "red", "NS"),
        (Point(4 * w_cell, 0 * h_cell + 1),Point( 5 * w_cell, 1 * h_cell), "red", "EW"),
        (Point(4 * w_cell, 2 * h_cell),Point( 5 * w_cell, 3 * h_cell), "blue", "NES"),
        (Point(4 * w_cell, 4 * h_cell),Point( 5 * w_cell, 5 * h_cell), "blue", "ESW"),
        (Point(4 * w_cell, 6 * h_cell),Point( 5 * w_cell, 7 * h_cell), "blue", "SWN"),
        (Point(4 * w_cell, 8 * h_cell),Point( 5 * w_cell, 9 * h_cell), "blue", "WNE"),
        (Point(6 * w_cell, 0 * h_cell + 1),Point( 7 * w_cell, 1 * h_cell), "black", "SWNE"),
    ]
    draw_cells = []
    for cell in cells:
        br, tl, fill_color, walls = cell
        draw_cell = Cell(bottom_right=br, top_left=tl, window=win)
        draw_cell.add_walls(walls=walls)
        draw_cell.draw(fill_color=fill_color)
        draw_cells.append(draw_cell)
    
    draw_cells[5].draw_move(draw_cells[10])


    win.wait_for_close()

if __name__ == "__main__":
    main()