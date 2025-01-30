from window import *

class Cell(object):

    def __init__(self,x1=None,x2=None,y1=None,y2=None,win=None):
        self.has_left_wall = 1
        self.has_right_wall = 1
        self.has_top_wall = 1
        self.has_bottom_wall = 1
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._visited = False
        if self._x1 is not None:
            self._center = Point((self._x1 + self._x2)//2,(self._y1 + self._y2)//2)
        self._win = win


    def draw(self,x1,x2,y1,y2):
        point_TL = Point(x1,y1)
        point_BL = Point(x1,y2)
        point_BR = Point(x2,y2)
        point_TR = Point(x2,y1)

        if self.has_left_wall:
            line = Line(point_TL,point_BL)
            line.draw(self._win.get_canvas(),fill_color='black')
        else:
            line = Line(point_TL,point_BL)
            line.draw(self._win.get_canvas(),fill_color='white')

        if self.has_bottom_wall:
            line = Line(point_BL,point_BR)
            line.draw(self._win.get_canvas(),fill_color='black')
        else:
            line = Line(point_BL,point_BR)
            line.draw(self._win.get_canvas(),fill_color='white')

        if self.has_right_wall:
            line = Line(point_BR,point_TR)
            line.draw(self._win.get_canvas(),fill_color='black')
        else:
            line = Line(point_BR,point_TR)
            line.draw(self._win.get_canvas(),fill_color='white')
        
        if self.has_top_wall:
            line = Line(point_TR,point_TL)
            line.draw(self._win.get_canvas(),fill_color='black')
        else:
            line = Line(point_TR,point_TL)
            line.draw(self._win.get_canvas(),fill_color='white')

    def draw_move(self, to_cell, undo=False):
            line = Line(self._center,to_cell._center)
            if undo:
                line.draw(self._win.get_canvas(),fill_color='gray')
            else:
                line.draw(self._win.get_canvas(),fill_color='red')