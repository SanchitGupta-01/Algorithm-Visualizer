from tkinter import *
from random import randrange
from GUI.resources.colors import *


class BarGUI(Frame):
    def __init__(self, master, func, **kw):
        # self.geometry(f"300x100+{int(self.winfo_screenwidth() / 2 - 150)}"
        #                      f"+{int(self.winfo_screenheight() / 2 - 100)}")
        # ^^^ or self.eval('tk::PlaceWindow . center')
        # self.minsize(250, 90)
        super().__init__(master, **kw)
        self.title = "bar"
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.__display_interface = Frame(self)
        self.__display_interface.configure(bg='grey')
        self.__display_interface.grid(row=0, column=0, sticky='nsew')

        master.bind("<Configure>", self.__on_window_resize)
        self.__canvas = Canvas(self.__display_interface, bg='grey')
        self.__canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.__input_container = Frame(self)
        self.__input_container.grid(row=0, column=0, sticky='nsew')
        self.__input_container.tkraise()

        # window width and height
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.__canvas_height = 0
        self.__canvas_width = 0

        # number of bars(input) and bar array
        self.__bar_count = 0
        self.__bars = []

        # hold for move when implemented
        # self.__hold = None
        # for controlling color.....
        self.__render_max = 0
        self.__resized = False
        self.__render_speed = IntVar(self.__canvas, 100)
        self.finished = False

        # sorting function to run
        self.__function_to_run = func
        self.__initiator()

    def __updater(self):
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.__canvas_height = self.__canvas.winfo_height()
        self.__canvas_width = self.__canvas.winfo_width()
        if self.__resized and self.finished:
            print("update")
            self.draw(iter([]))
            self.__resized = False
        self.after(10, self.__updater)

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
            # self.title(self.title)
            # self.__input_container.forget()
            self.__create_bars()
            self.__display_interface.tkraise()

        self.__updater()

    def __create_bars(self):
        # self.geometry(f"600x400+{int(self.winfo_screenwidth() / 2 - 300)}"
        #                      f"+{int(self.winfo_screenheight() / 2 - 250)}")

        self.__render_max = self.__bar_count

        # adding bars to array  ----- (None for future use.. if want to add bars as widgets)
        for i in range(self.__bar_count):
            self.__bars.append((None,
                                randrange(25, self.__canvas.winfo_reqheight()) / self.__canvas.winfo_reqheight()))

        # rendering according to function to run
        self.__canvas.after(20, self.draw, self.__function_to_run())

    def __render_bars(self, active_bars: tuple = (), swap=False,
                      remaining_color=ORANGE, swap_color=RED,
                      active_color=GREEN, sorted_color=BLUE,
                      finished_color=GREY):
        self.__canvas.delete('all')

        bar_width = (self.__canvas.winfo_width() - 4) / self.__bar_count
        active = list(active_bars)

        for i, bar in enumerate(self.__bars):
            if i < self.__render_max or len(active) == 0:
                b_color = remaining_color
            else:
                b_color = sorted_color

            if i in active:
                if i == self.__render_max - 1 and not swap:
                    self.__render_max -= 1
                if not swap:
                    b_color = active_color
                else:
                    b_color = swap_color

            if self.finished:
                b_color = finished_color

            bd = self.__canvas
            bd.create_rectangle(i * bar_width + 4, bd.winfo_height() - bar[1] * bd.winfo_height(),
                                (i + 1) * bar_width - 2, bd.winfo_height(),
                                fill=b_color, outline=b_color)

    def __on_window_resize(self, e):
        # w_scale = e.width / self.width
        # h_scale = e.height / self.height
        # self.width = e.width
        # self.height = e.height
        # self.__canvas.scale('all', 0, 0, w_scale, h_scale)
        self.__resized = True

    def draw(self, states: iter):
        try:
            self.__render_bars(*next(states))
        except StopIteration:
            self.__canvas.after(self.__render_speed.get(), self.__render_bars)
            self.finished = True
            print("completed")
            return
        self.__canvas.after(self.__render_speed.get(), self.draw, states)

    # todo implement method move_bars
    # def move_bars(self, i, j):
    #     yield
    #     x, y = j, i
    #     pass
    #     #
    #     # def update():
    #     #     return
    #     #     self.__bar_draw.after(10, update)

    # def set_title(self, s):
    #     self.title = s

    def set_render_speed(self, speed):
        self.__render_speed.set(speed)

    def set_function_to_run(self, func, *args, **kwargs):
        self.__function_to_run = lambda i=0: func(*args, **kwargs)

    def get_bars(self):
        return self.__bars
