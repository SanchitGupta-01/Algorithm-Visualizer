from GUI.visualizers.grid import *
from Searching.A_Star.node import Node


class AStarPathfinder(GridGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         lambda i=0: self.a_star_pathfinder(
                             self.get_grid_nodes().get_start_node(),
                             self.get_grid_nodes().get_goal_node()
                         ), Node, **kwargs)
        self.title = 'A* Pathfinder Algorithm'
        # self.set_cost()

    @staticmethod
    def a_star_pathfinder(start: Node, goal: Node):
        open_list = [start]
        closed_list = []

        while len(open_list) is not 0:
            current_node = open_list.pop()

            if current_node is goal:
                break

            neighbors = current_node.get_neighbors()

            for node in neighbors:
                if node in closed_list:
                    continue

                cost = node.g_cost  # distance b/w node and current node
                new_g = current_node.g_cost + cost
                xc, yc = node.position()
                xg, yg = goal.position()
                new_h = abs(xc - xg) + abs(yc - yg)  # Manhattan distance
                # new_h = math.sqrt((xc - xg)**2 + (yc - yg)**2)        # Euclidean distance
                new_f = new_g + new_h

                if node in open_list and new_f > node.f_cost:
                    continue
                else:
                    node.g_cost, node.h_cost, node.f_cost = new_g, new_h, new_f
                    node.set_color('yellow')
                    open_list.append(node)
                    node.set_parent(current_node)
                    open_list = sorted(open_list, key=lambda i=0: i.f_cost, reverse=True)
                    yield node

            closed_list.append(current_node)
            current_node.set_color('orange')
            yield current_node

    # @staticmethod
    # def set_cost(buttons=0, cost=()):
    #     pass

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
