import pygame

class Size:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.center = (x + width // 2, y + height // 2)
        self.right = x+width
        self.left = x
        self.top = y
        self.bottom = y+height
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    
    @x.setter
    def x(self, value):
        self._x = value
    @y.setter
    def y(self, value):
        self._y = value
    @width.setter
    def width(self, value):
        self._width = value
    @height.setter
    def height(self, value):
        self._height = value