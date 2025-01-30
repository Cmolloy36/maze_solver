from window import *
from cell import *
from maze import *


def main():
    num_rows = 20
    num_cols = 20
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win,seed=0)

    res = maze.solve()

    if res == True:
        print("Maze Solved!")
    else:
        print("Unsolvable Maze...")

    '''Test drawing line from cell centers

    cell_T = Cell(300,500,100,300,win)
    # cell_L.has_left_wall = 0
    # cell_L.has_bottom_wall = 0
    # cell_L.has_right_wall = 0
    # cell_L.has_top_wall = 0
    cell_T.draw() #provide x1,x2,y1,y2


    cell_B = Cell(200,400,400,600,win)
    cell_B.draw()

    cell_R = Cell(500,700,300,500,win)
    cell_R.draw()


    cell_T.draw_move(cell_B) #red
    cell_R.draw_move(cell_B,undo=True) #gray
    '''

    '''
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
    '''

    #test window closure
    win.wait_for_close()

if __name__ == '__main__':
    main()