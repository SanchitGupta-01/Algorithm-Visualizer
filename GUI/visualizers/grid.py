from GUI.resources.colors import *
from tkinter import *
from GUI.gridoptions import GridOptions


class GridGUI(Frame):
    def __init__(self, master, func, node, **kw):
        super().__init__(master, **kw)
        self.Node = node
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.__title = "grid"

        master.bind("<Configure>", lambda i=0: self.__on_grid_resize())
        master.bind("<space>", lambda i=0: self.pause() if self.__run_state else self.start())
        master.bind("<Return>", lambda i=0: self.start())
        master.bind("<BackSpace>", lambda i=0: self.stop() if not self.rows == 0 else None)
        master.bind("<Right>", lambda i=0: self.next_step())
        master.bind("<Left>", lambda i=0: self.prev_step())

        self.__input_container = Frame(self)
        self.__input_container.pack(fill=BOTH, expand=YES)

        self.__canvas = Canvas(self)

        self.rows = 0
        self.columns = 0
        self.__grid_nodes: (GridNodes, None) = None
        self.prev_states = []

        self.resized = False
        self.__run_state = False
        self.finished = False
        self.states_captured = False
        self.__stop_run = False
        self.__render_speed = IntVar(self.__canvas, 75)
        self.step = False
        self.step_index = 0  # current access point, i.e. access from this pt if not exist get next state

        self.__function_to_run = func
        self.option_active = None
        self.last_activated_node = None
        self.__initiator()

    def __updater(self):
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        if self.__stop_run:
            self.__grid_nodes = GridNodes(node=self.Node, rows=self.rows,
                                          columns=self.columns, color=GREY)
            self.__set_grid()
        if self.resized or (not self.__run_state and self.finished):
            self.__canvas.delete('all')
            self.__set_grid()
            self.resized = False
        self.after(self.get_render_speed(), self.__updater)

    def __initiator(self):
        self.__input_container.columnconfigure(0, weight=1)
        self.__input_container.columnconfigure(1, weight=2)
        self.__input_container.rowconfigure(3, weight=1)

        r_label = Label(self.__input_container,
                        text="Rows: ",
                        font="helvetica 15")  # rows input
        r_entry = Entry(self.__input_container,
                        font="helvetica 11")

        c_label = Label(self.__input_container,
                        text="Columns: ",
                        font="helvetica 15")  # columns input
        c_entry = Entry(self.__input_container,
                        font="helvetica 11")

        e_label = Label(self.__input_container,
                        font="helvetica 10")  # error label

        make = Button(self.__input_container,
                      text="Make Grid",
                      font="helvetica 16",
                      command=lambda i=0: get_data())

        r_label.grid(row=0, column=0, sticky='nsew')
        r_entry.grid(row=0, column=1, sticky='nsew')
        r_entry.bind('<Return>', lambda i=0: c_entry.focus_set())
        r_entry.focus_set()

        c_label.grid(row=1, column=0, sticky='nsew')
        c_entry.grid(row=1, column=1, sticky='nsew')
        c_entry.bind('<Return>', lambda i=0: c_entry.after(70, get_data))

        e_label.grid(row=2, column=0, columnspan=2)

        make.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=45, pady=30)

        def get_data():
            try:
                self.rows = int(r_entry.get())
                self.columns = int(c_entry.get())
                check1 = self.rows > 70 or self.columns > 70  # self.height  self.width
                check2 = self.rows <= 0 or self.columns <= 0
                if check1 or check2:
                    raise ValueError
            except ValueError:
                e_label['text'] = "Sorry, Enter Valid Numbers!!!"
                return
            self.__grid_nodes = GridNodes(node=self.Node, rows=self.rows,
                                          columns=self.columns, color=GREY)
            self.__input_container.destroy()
            self.__updater()
            self.__create_grid()

    def __create_grid(self):
        self.__canvas.after(50, self.__set_grid)
        self.__canvas.configure(bg='black')
        self.__canvas.pack(fill=BOTH, expand=True, padx=1, pady=1)
        self.after(70, self.__update_grid, self.__function_to_run())
        self.__canvas.bind('<Button-3>', self.show_grid_options)
        self.__canvas.bind('<B1-Motion>', self.execute_grid_option)
        self.__canvas.bind('<Button-1>', self.execute_grid_option)

    def __set_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                width = self.width / self.columns
                height = self.height / self.rows
                t = self.__canvas.create_rectangle(width * j, height * i,
                                                   width * (j + 1), height * (i + 1),
                                                   fill=self.__grid_nodes.get_color(i, j),
                                                   outline='black')
                self.__grid_nodes(i, j).set_id(t)

    def __update_grid(self, state):  # state: node, iter state
        try:
            assert not self.__stop_run, 'stop'
            if not self.step:
                assert self.__run_state, 'pause'
            if self.states_captured or not self.step_index == len(self.prev_states):
                self.next_step(stop=False)
                raise AssertionError
            self.step = False
            current_state: tuple = next(state)
            self.step_index += 1
            self.prev_states.append(current_state)
            current_state[0].set_color(current_state[2])
            self.__canvas.itemconfig(current_state[0].id, fill=current_state[0].get_color())
        except StopIteration:
            self.__run_state = False
            self.finished = True
            print('finished')
            return
        except AssertionError as err:
            if str(err) is 'stop':
                return

        self.after(self.__render_speed.get(), self.__update_grid, state)

    def __on_grid_resize(self):
        self.resized = True

    def show_grid_options(self, event):
        within = BooleanVar()
        within.set(True)

        def remove(w, opt, wait=True):
            if not wait and not w.get():
                opt.destroy()
            if wait:
                w.set(False)
                opt.after(200, remove, within, opt, False)

        options = GridOptions(self.__canvas, self.button_action)
        options.place(x=event.x - 2, y=event.y - 2)
        options.bind('<Leave>', lambda i=0: remove(within, options))
        options.bind('<Enter>', lambda i=0: within.set(True))

    def button_action(self, action):
        self.option_active = action

    def execute_grid_option(self, event):
        if self.option_active:
            width = self.width / self.columns
            height = self.height / self.rows
            j, i = event.x // width, event.y // height
            current = self.__grid_nodes(i, j)
            if current is self.last_activated_node:
                return
            self.last_activated_node = current
            self.option_active(current)

    def get_grid_nodes(self):
        return self.__grid_nodes

    def set_render_speed(self, speed):
        self.__render_speed.set(speed)

    def get_render_speed(self):
        return self.__render_speed.get()

    def start(self):
        if not (self.rows == 0 or self.columns == 0):
            self.__run_state = True
            self.option_active = None

    def pause(self):
        self.__run_state = False
        self.option_active = None

    def stop(self):
        if not self.finished:
            self.__stop_run = True
        self.__run_state = False
        self.finished = False

    def next_step(self, stop=True):
        if self.finished or self.step:
            return
        if stop:
            self.pause()
        self.option_active = None
        i = self.step_index
        if i < 0 or i > len(self.prev_states):
            return
        if i == len(self.prev_states):
            self.step = True
            return
        next_state = self.prev_states[i]  # next_state->(node,from_col,to_col)
        next_state[0].set_color(next_state[2])
        self.__canvas.itemconfig(next_state[0].id, fill=next_state[0].get_color())
        self.step_index += 1

    def prev_step(self, stop=True):
        if self.finished:
            self.finished = False
            self.__stop_run = False
            self.step = False
            self.__update_grid(iter(()))
        self.option_active = None
        if stop:
            self.pause()
        i = self.step_index
        if i <= 0:
            return
        prev_state = self.prev_states[i - 1]  # prev_state->(node,from_col,to_color)
        prev_state[0].set_color(prev_state[1])
        self.__canvas.itemconfig(prev_state[0].id, fill=prev_state[0].get_color())
        self.step_index -= 1


class GridNodes:
    def __init__(self, node, rows, columns, start=None, goal=None, color=GREY):
        self.rows = rows
        self.columns = columns
        self.__nodes = {}
        for i in range(rows):
            for j in range(columns):
                self.__nodes[(i, j)] = node(self, i, j, 1, color)
        self.__goal_node = None
        self.set_goal_node(goal if goal is not None else self.__nodes[(self.rows - 1, self.columns - 1)])
        self.__start_node = None
        self.set_start_node(start if start is not None else self.__nodes[(0, 0)])

    def __call__(self, x, y):
        return self.__nodes[(x, y)]

    def get_nodes(self):
        assert self.__nodes is not None, 'nodes not set'
        return self.__nodes

    def get_color(self, i, j):
        return self.__nodes[(i, j)].get_color()

    def set_color(self, i, j, color):
        self.__nodes[(i, j)].set_color(color)

    def set_start_node(self, start):
        start.set_color('blue', True)
        self.__start_node = start

    def set_goal_node(self, goal):
        goal.set_color('red', True)
        self.__goal_node = goal

    def get_start_node(self):
        return self.__start_node

    def get_goal_node(self):
        return self.__goal_node

    def get_neighbors(self, x, y):
        adjacent = ((1, 0), (0, 1), (0, -1), (-1, 0))
        #            (-1, 1), (1, -1), (1, 1), (-1, -1))  # if want to include edges
        ad_nodes = []
        for ad in adjacent:
            i, j = x + ad[0], y + ad[1]
            if 0 <= i < self.rows and 0 <= j < self.columns:
                node = self.__nodes[(i, j)]
                if not node.wall:
                    ad_nodes.append(node)

        return ad_nodes
