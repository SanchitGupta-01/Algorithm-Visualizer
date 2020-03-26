from GUI.visualizers.grid import *


class PathFinder(GridGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         lambda i=0: self.a_star_pathfinder(
                             self.get_grid_nodes().get_start_node(),
                             self.get_grid_nodes().get_goal_node()
                         ), **kwargs)
        self.title = 'A* Pathfinder Algorithm'
        # self.set_cost()

    def a_star_pathfinder(self, start, goal):
        nodes: dict = self.get_grid_nodes().get_nodes()
        open_list = sorted(list(nodes.keys()), key=lambda i=0: i.f)
        closed_list = []

        while len(open_list) is not 0:
            next_node = nodes[open_list.pop()]
            neighbors = next_node.get_neighbors()

            for node in neighbors:
                if node is goal:
                    pass
                node = node.copy()
                cost = 1
                node.g = next_node.g + cost
                node.h = 0
                node.f = node.g + node.h
                pos = node.position()

                if pos in open_list and nodes[pos].f < node.f:
                    continue

                if pos in closed_list and node.f > nodes[pos]:
                    continue
                else:
                    open_list.append(pos)
                    open_list.sort(key=lambda i=0: i.f)

            closed_list.append(next_node.position())

        print(closed_list)

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


# PathFinder().display()
