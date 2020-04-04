from GUI.resources.colors import *
from tkinter import *


class GridGUI(Frame):
    def __init__(self, master, func, node, **kw):
        super().__init__(master, **kw)
        self.node = node
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.__title = "grid"

        master.bind("<Configure>", lambda i=0: self.__on_grid_resize())

        self.__input_container = Frame(self)
        self.__input_container.pack(fill=BOTH, expand=YES)

        self.__canvas = Canvas(self)

        self.rows = 0
        self.columns = 0
        self.__grid_nodes: (GridNodes, None) = None

        self.resized = False
        self.__run_state = False
        self.finished = False
        self.__stop_draw = False
        self.__render_speed = IntVar(self.__canvas, 10)

        self.__initiator()

    def __updater(self):
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        if self.resized:
            self.__canvas.delete('all')
            if self.__stop_draw:
                self.__grid_nodes = GridNodes(node=self.node, rows=self.rows,
                                              columns=self.columns, color=GREY)
            self.__set_grid()
            self.resized = False
        self.after(self.__render_speed.get(), self.__updater)

    def __initiator(self):
        Grid.columnconfigure(self.__input_container, 0, weight=1)
        Grid.columnconfigure(self.__input_container, 1, weight=2)
        Grid.rowconfigure(self.__input_container, 3, weight=1)

        r_label = Label(self.__input_container, text="Rows: ")  # rows input
        r_label.grid(row=0, column=0, sticky='nsew')
        r_entry = Entry(self.__input_container)
        r_entry.grid(row=0, column=1, sticky='nsew')

        c_label = Label(self.__input_container, text="Columns: ")  # columns input
        c_label.grid(row=1, column=0, sticky='nsew')
        c_entry = Entry(self.__input_container)
        c_entry.grid(row=1, column=1, sticky='nsew')

        e_label = Label(self.__input_container)  # error label
        e_label.grid(row=2, column=0, columnspan=2)

        make = Button(self.__input_container, text="Make Grid",
                      command=lambda i=0: __get_data(r_entry, c_entry))
        make.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=45)

        def __get_data(r, c):
            try:
                self.rows = int(r.get())
                self.columns = int(c.get())
                if self.rows > self.height or self.columns > self.width:
                    raise ValueError
            except ValueError:
                e_label['text'] = "Sorry, Enter Valid Numbers!!!"
                return
            self.__grid_nodes = GridNodes(node=self.node, rows=self.rows,
                                          columns=self.columns, color=GREY)
            self.__input_container.forget()
            self.__create_grid()
            self.add_controls()

        self.__updater()

    def __create_grid(self):
        self.__canvas.after(50, self.__set_grid)
        self.__canvas.configure(bg='black')
        self.__canvas.pack(fill=BOTH, expand=True)

    def __set_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                width = self.width / self.columns
                height = self.height / self.rows
                self.__canvas.create_rectangle(width * j, height * i,
                                               width * (j + 1), height * (i + 1),
                                               fill=self.__grid_nodes.get_color(i, j),
                                               outline='black')

    def __on_grid_resize(self):
        self.resized = True

    def add_controls(self):
        pass

    def get_grid_nodes(self):
        return self.__grid_nodes

    def set_render_speed(self, speed):
        self.__render_speed.set(speed)

    def get_render_speed(self):
        return self.__render_speed.get()

    def start(self):
        if not (self.rows == 0 or self.columns == 0):
            self.__run_state = True

    def pause(self):
        self.__run_state = False

    def stop(self):
        if not self.finished:
            self.__stop_draw = True
        self.__run_state = False
        self.finished = False
        self.__set_grid()


class GridNodes:
    def __init__(self, node, rows, columns, start=None, goal=None, color=GREY):
        self.rows = rows
        self.columns = columns
        self.__goal_node = goal
        self.__start_node = start
        self.__nodes = {}
        for i in range(rows):
            for j in range(columns):
                self.__nodes[(i, j)] = node(self, i, j, 1, color)

    def get_nodes(self):
        assert self.__nodes is not None, 'nodes not set'
        return self.__nodes

    def get_color(self, i, j):
        return self.__nodes[(i, j)].color

    def set_color(self, i, j, color):
        self.__nodes[(i, j)].color = color

    def set_start_node(self, start):
        self.__start_node = start

    def set_goal_node(self, goal):
        self.__goal_node = goal

    def get_start_node(self):
        return self.__start_node

    def get_goal_node(self):
        return self.__goal_node

    @staticmethod
    def get_distance():
        pass

    def get_neighbors(self, x, y):
        adjacent = ((-1, -1), (0, -1), (1, -1), (-1, 0),
                    (1, 0), (-1, 1), (0, 1), (1, 1))
        ad_nodes = []
        for ad in adjacent:
            if 0 <= x + ad[0] < self.columns and 0 <= y + ad[1] < self.rows:
                node = self.__nodes[(x + ad[0], y + ad[1])]
                ad_nodes.append(node)
                node.parent = self.__nodes[(x, y)]

        return ad_nodes
