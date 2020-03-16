from visualizers.grid import *
from heapq import *

# get start, end, blockage


class PathFinder(GridGUI):
    def __init__(self):
        super().__init__(lambda i=0: self.a_star_pathfinder(self.get_grid_nodes().get_start_node(),
                                                            self.get_grid_nodes().get_goal_node()))
        # self.set_cost()

    def a_star_pathfinder(self, start, goal):
        nodes: GridNodes = self.get_grid_nodes()
        open_list = []
        closed_list = []
        heappush(open_list, start)
        while len(open_list) is not 0:
            next_node = open_list.pop()
            neighbors = next_node.get_neighbors()
            for ad in neighbors:
                if ad is nodes.get_goal_node():
                    cost = 1
                    ad.g = next_node.g + cost
                    # ad.h =
                    ad.f = ad.g

    @staticmethod
    def set_cost(buttons=0, cost=()):
        pass

    # def __add_action_bar(self):
    #     # todo: implement these
    #     def start_button_action(button):
    #         pass
    #
    #     def end_button_action(button):
    #         pass
    #
    #     def add_stop_button_action(button):
    #         pass
    #
    #     def add_wall_button_action(button):
    #         pass
    #
    #     def add_weight_button_action():
    #         pass
    #
    #     frame = Frame(self.get_root())
    #     start = Button(frame, text='Start\nPoint', command=self.set_button_action(start_button_action))\
    #         .pack(side=LEFT)
    #     add_stop = Button(frame, text='Add\nStop', command=self.set_button_action(add_stop_button_action))\
    #         .pack(side=LEFT)
    #     add_weights = Button(frame, text='Add\nWeight', command=self.set_button_action(add_weight_button_action))\
    #         .pack(side=LEFT)
    #     add_wall = Button(frame, text='Add\nWall', command=self.set_button_action(add_wall_button_action))\
    #         .pack(side=LEFT)
    #     end = Button(frame, text='Destination', command=self.set_button_action(end_button_action))\
    #         .pack(side=LEFT)
    #     frame.pack(side=BOTTOM)


PathFinder().display()
