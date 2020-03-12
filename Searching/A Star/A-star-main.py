from visualizers.grid import *


# get start, end, blockage


class PathFinder(GridGUI):
    def __init__(self):
        super().__init__()
        buttons = self.get_buttons()
        # self.set_cost()

    @staticmethod
    def set_cost(buttons=0, cost=()):
        pass

    def __add_action_bar(self):
        # todo: implement these
        def start_button_action(button):
            pass

        def end_button_action(button):
            pass

        def add_stop_button_action(button):
            pass

        def add_wall_button_action(button):
            pass

        def add_weight_button_action():
            pass

        frame = Frame(self.get_root())
        start = Button(frame, text='Start\nPoint', command=self.set_button_action(start_button_action))\
            .pack(side=LEFT)
        add_stop = Button(frame, text='Add\nStop', command=self.set_button_action(add_stop_button_action))\
            .pack(side=LEFT)
        add_weights = Button(frame, text='Add\nWeight', command=self.set_button_action(add_weight_button_action))\
            .pack(side=LEFT)
        add_wall = Button(frame, text='Add\nWall', command=self.set_button_action(add_wall_button_action))\
            .pack(side=LEFT)
        end = Button(frame, text='Destination', command=self.set_button_action(end_button_action))\
            .pack(side=LEFT)
        frame.pack(side=BOTTOM)


PathFinder().display()
