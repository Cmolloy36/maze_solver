from window import *


def main():
    win = Window(800, 600)

    #test points and line drawing
    point1 = Point(200,200)
    point2 = Point(200,400)
    point3 = Point(600,400)
    point4 = Point(600,200)

    line1 = Line(point1,point2)
    line2 = Line(point2,point3)
    line3 = Line(point3,point4)
    line4 = Line(point4,point1) 

    win.draw_line(line1,'green')
    win.draw_line(line2,'blue')
    win.draw_line(line3,'black')
    win.draw_line(line4,'red')

    #test window closure
    win.wait_for_close()

if __name__ == '__main__':
    main()