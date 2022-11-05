from shape import *
from time import sleep
class Circle(Shape):
    def __init__(self, screen, center_x, center_y, radius, color='BLUE',  background_color ="WHITE"):
        super().__init__(screen, color,  background_color ="WHITE")
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
    def draw(self):
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()
    def remove(self):
        py.draw.circle(self.screen, self.bg, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()
    def move(self, x, y):
        self.remove()
        self.__center_x +=x
        self.__center_y +=y
        self.draw()
    def change_size(self, val):
        self.remove()
        self.__radius +=self.__radius +(self.__radius * (val/100))
        self.draw()
    def get_center(self):
        return (self.__center_x, self.__center_y)
    def get_radius(self):
        return self.__radius
    def set_center(self, x, y):
        self.__center_x =x
        self.__center_y =y
    def set_radius(self, rad):
        self.__radius =rad


