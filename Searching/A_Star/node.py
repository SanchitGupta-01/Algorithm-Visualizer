from GUI.visualizers.grid import GridNodes


class Node:
    def __init__(self, master, y_index, x_index, g_cost, color):
        self.g_cost, self.h, self.f = g_cost, 99999999, 99999999
        self.master: GridNodes = master
        self.parent = None
        self.y_index = y_index
        self.x_index = x_index
        self.color = color

    def position(self):
        return self.x_index, self.y_index

    def get_neighbors(self):
        return self.master.get_neighbors(*self.position())
