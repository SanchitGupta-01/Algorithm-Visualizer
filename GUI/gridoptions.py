from tkinter import *

from GUI.resources.colors import GREY


class GridOptions(Frame):
    def __init__(self, master, action, *args, **kw):
        super().__init__(master, *args, **kw)
        self.active_option = None
        l_frame = LabelFrame(self,
                             text='Grid Options',
                             padx=1, pady=1,
                             labelanchor='n')
        start = Button(l_frame,
                       text='Start\nPoint',
                       width=10,
                       command=lambda i=0: action(self.set_start))
        add_stop = Button(l_frame,
                          text='Add\nStop',
                          width=10,
                          command=lambda i=0: action(self.set_mid_stop))
        add_weights = Button(l_frame,
                             text='Add\nWeight',
                             width=10,
                             command=lambda i=0: action(self.add_weight))
        add_wall = Button(l_frame,
                          text='Add/Remove\nWall',
                          width=10,
                          command=lambda i=0: action(self.add_wall))
        end = Button(l_frame,
                     text='Destination',
                     width=10,
                     command=lambda i=0: action(self.set_end))

        l_frame.rowconfigure((0, 1), weight=1)
        l_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        l_frame.pack(fill=BOTH, expand=True)
        start.grid(row=0, column=0,
                   columnspan=2, sticky='nsew', padx=1, pady=1)
        add_stop.grid(row=0, column=2,
                      columnspan=2, sticky='nsew', padx=1, pady=1)
        end.grid(row=0, column=4,
                 columnspan=2, sticky='nsew', padx=1, pady=1)
        add_weights.grid(row=1, column=1,
                         columnspan=2, sticky='nsew', padx=1, pady=1)
        add_wall.grid(row=1, column=3,
                      columnspan=2, sticky='nsew', padx=1, pady=1)

    def set_start(self, node):
        g_nodes = self.master.master.get_grid_nodes()  # GridNodes obj, .master gives parent obj
        g_nodes.get_start_node().set_color(GREY, True)
        self.master.itemconfig(g_nodes.get_start_node().id, fill=node.get_color())
        g_nodes.set_start_node(node)
        self.master.itemconfig(node.id, fill=node.get_color())

    def set_end(self, node):
        g_nodes = self.master.master.get_grid_nodes()  # GridNodes obj
        g_nodes.get_goal_node().set_color(GREY, True)
        self.master.itemconfig(g_nodes.get_goal_node().id, fill=node.get_color())
        g_nodes.set_goal_node(node)
        self.master.itemconfig(node.id, fill=node.get_color())

    @staticmethod
    def set_mid_stop(self, button):
        pass

    def add_wall(self, node):
        if not node.start_or_end():
            node.wall = not node.wall
            self.master.itemconfig(node.id, fill=node.get_color())

    @staticmethod
    def add_weight(self, button):
        pass
