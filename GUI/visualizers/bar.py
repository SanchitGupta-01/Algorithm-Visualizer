from tkinter import *
from random import randrange
from GUI.resources.colors import *


class BarGUI(Frame):
    def __init__(self, master, func, **kw):
        super().__init__(master, **kw)
        self.title = "bar"
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.__display_interface = Frame(self)
        self.__display_interface.configure(bg='grey')
        self.__display_interface.grid(row=0, column=0, sticky='nsew')

        master.bind("<Configure>", lambda i=0: self.__on_window_resize())
        master.bind("<space>", lambda i=0: self.pause() if self.__run_state else self.start())
        master.bind("<Return>", lambda i=0: self.start())
        master.bind("<Right>", lambda i=0: self.next_step())
        master.bind("<Left>", lambda i=0: self.prev_step())

        self.__canvas = Canvas(self.__display_interface, bg='grey')
        self.__canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.__input_container = Frame(self)
        self.__input_container.grid(row=0, column=0, sticky='nsew')
        self.__input_container.tkraise()

        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.__canvas_height = 0
        self.__canvas_width = 0

        self.__bar_count = 0
        self.__bars = []
        self.prev_states = [(tuple(), False, GREY)]
        self.__finished_bars = []

        self.__resized = False
        self.__render_speed = IntVar(self.__canvas, 10)
        self.finished = False
        self.__run_state = False
        self.__stop_draw = False
        self.step = False
        self.step_index = 0

        self.__function_to_run = func
        self.__initiator()

    def __updater(self):
        if self.__resized and self.finished:
            print("update")
            self.draw(iter([]))
            self.__resized = False
        self.after(20, self.__updater)

    def __initiator(self):
        Grid.columnconfigure(self.__input_container, 0, weight=1)
        Grid.columnconfigure(self.__input_container, 1, weight=2)
        Grid.rowconfigure(self.__input_container, 0, weight=1)
        Grid.rowconfigure(self.__input_container, 2, weight=1)

        bc_label = Label(self.__input_container, text="Bars: ")
        bc_label.grid(row=0, column=0, sticky='nsew', pady=5)

        e_label = Label(self.__input_container)
        e_label.grid(row=1, column=0, columnspan=2, pady=5)

        bc_entry = Entry(self.__input_container)
        bc_entry.grid(row=0, column=1, sticky='ew', pady=5, padx=50)

        make = Button(self.__input_container, text="Visualize!!!",
                      command=lambda i=0: get_data(bc_entry))
        make.grid(row=2, column=0, columnspan=2, pady=5, sticky='nsew')

        def get_data(bc):
            try:
                self.__bar_count = int(bc.get())
                assert self.__bar_count != 0
            except (ValueError, AssertionError):
                e_label['text'] = "Sorry, Enter Valid Number!!!"
                return
            self.__create_bars()
            self.__display_interface.tkraise()

        self.__updater()

    def __create_bars(self):
        self.__bars = []
        self.prev_states = [(tuple(), False, GREY)]
        self.step_index = 0
        self.__finished_bars = []
        for i in range(self.__bar_count):
            self.__bars.append(randrange(25, self.__canvas.winfo_reqheight()) / self.__canvas.winfo_reqheight())

        # rendering according to function to run
        self.__canvas.after(self.__render_speed.get() + 20, self.draw, self.__function_to_run())

    def __render_bars(self, active_bars: tuple = (), swap=False,
                      remaining_color=ORANGE, swap_color=RED,
                      active_color=GREEN, sorted_color=BLUE,
                      finished_color=GREY, outline_color='darkgrey'):
        self.__canvas.delete('all')

        bar_width = (self.__canvas.winfo_width() - 4) / self.__bar_count
        active = list(active_bars)

        for i, bar in enumerate(self.__bars):
            if bar not in self.__finished_bars or len(active) == 0:
                b_color = remaining_color
                outline_color = remaining_color if bar_width < 1 else outline_color
            else:
                b_color = sorted_color

            if i in active:
                if not swap:
                    b_color = active_color
                else:
                    b_color = swap_color
                    outline_color = swap_color if bar_width < 1 else outline_color

            if self.finished:
                b_color = finished_color

            bd = self.__canvas
            bd.create_rectangle(i * bar_width, bd.winfo_height() - bar * bd.winfo_height(),
                                (i + 1) * bar_width, bd.winfo_height(),
                                fill=b_color, outline=outline_color)

    def __on_window_resize(self):
        self.__resized = True

    def draw(self, states: iter):
        try:
            if self.__stop_draw:
                raise StopIteration

            if self.step_index == len(self.prev_states) - 1:
                if self.__run_state or self.step:
                    prev = next(states)
                    self.prev_states.append(prev)
                    self.__render_bars(*prev)
                    self.step_index += 1
                else:
                    self.__render_bars(*self.prev_states[self.step_index])
                self.step = False
            else:
                if self.__run_state:
                    self.next_step()
                self.__render_bars(*self.prev_states[self.step_index])
                self.step = False

        except StopIteration:
            self.__canvas.after(self.__render_speed.get(),
                                self.__render_bars(remaining_color=GREY))
            self.finished = True if not self.__stop_draw else False
            self.__stop_draw = False
            print("stop/completed")
            return
        self.__canvas.after(self.__render_speed.get(), self.draw, states)

    def set_render_speed(self, speed):
        self.__render_speed.set(speed)

    def get_render_speed(self):
        return self.__render_speed.get()

    # def set_function_to_run(self, func, *args, **kwargs):
    #     self.__function_to_run = lambda i=0: func(*args, **kwargs)

    def add_finished_bar(self, i):
        self.__finished_bars.append(self.__bars[i])

    def get_bars(self):
        return self.__bars

    def start(self):
        if not self.__bar_count == 0:
            self.__run_state = True

    def pause(self):
        self.__run_state = False

    def stop(self):
        if not self.finished:
            self.__stop_draw = True
        self.__run_state = False
        self.finished = False
        self.step = False
        self.__create_bars()

    def next_step(self):
        if self.finished or self.step:
            return
        if not self.__run_state:
            self.pause()
        i = self.step_index
        if i < 0 or i >= len(self.prev_states):
            return
        if i < len(self.prev_states) - 1:
            if self.prev_states[i][1]:
                cur = self.prev_states[i][0]  # get swap info -> tuple() in every state
                self.__bars[cur[0]], self.__bars[cur[1]] = self.__bars[cur[1]], self.__bars[cur[0]]
            self.step_index += 1
        self.step = True

    def prev_step(self):
        if self.step:
            return
        self.pause()
        i = self.step_index
        if i <= 0:
            return
        if self.prev_states[i - 1][1]:
            prev = self.prev_states[i - 1][0]
            self.__bars[prev[0]], self.__bars[prev[1]] = self.__bars[prev[1]], self.__bars[prev[0]]

        self.step_index -= 1
        self.step = True
