from graphics import Window, Point, Line

def main():
    app_window = Window(800, 600)

    point1 =  Point(10, 30)
    point2 = Point(40, 70)

    line = Line(point1, point2)

    app_window.draw_line(line, "black")

    app_window.wait_for_close()

if __name__ == "__main__":
    main()
    