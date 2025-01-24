from window import *

class Cell(object):

    def __init__(self,x1,x2,y1,y2,win):
        self.has_left_wall = 1
        self.has_right_wall = 1
        self.has_top_wall = 1
        self.has_bottom_wall = 1
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win


    def draw(self):
        point_TL = Point(self._x1,self._y1)
        point_BL = Point(self._x1,self._y2)
        point_BR = Point(self._x2,self._y2)
        point_TR = Point(self._x2,self._y1)

        if self.has_left_wall:
            line = Line(point_TL,point_BL)
            line.draw(self._win.get_canvas(),fill_color='black')
        if self.has_bottom_wall:
            line = Line(point_BL,point_BR)
            line.draw(self._win.get_canvas(),fill_color='black')
        if self.has_right_wall:
            line = Line(point_BR,point_TR)
            line.draw(self._win.get_canvas(),fill_color='black')
        if self.has_top_wall:
            line = Line(point_TR,point_TL)
            line.draw(self._win.get_canvas(),fill_color='black')