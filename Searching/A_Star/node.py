from GUI.visualizers.grid import GridNodes
from GUI.resources.colors import *


class Node:
    def __init__(self, master, x_index, y_index, g_cost, color):
        self.g_cost, self.h_cost, self.f_cost = g_cost, 99999999, 99999999
        self.master: GridNodes = master
        self.parent = None
        self.y_index = y_index
        self.x_index = x_index
        self.__color = color
        self.id = None
        self.__wall = False

    @property
    def wall(self):
        return self.__wall

    @wall.setter
    def wall(self, b: bool):
        self.__wall = b
        color = 'brown' if b else GREY
        self.set_color(color)

    def position(self):
        return self.x_index, self.y_index

    def get_neighbors(self):
        return self.master.get_neighbors(*self.position())

    def set_parent(self, node):
        self.parent = node

    def set_id(self, i):
        self.id = i

    def start_or_end(self):
        return self is self.master.get_start_node() or self is self.master.get_goal_node()

    def set_color(self, c, skip_check=False):
        if (not skip_check) and self.start_or_end():
            return
        self.__color = c

    def get_color(self):
        return self.__color
