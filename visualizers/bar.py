from tkinter import *
from random import randrange
from visualizers.colors import *
import time


class BarGUI:
    def __init__(self, func):
        self.__root = Tk()
        self.__root.geometry(f"300x100+{int(self.__root.winfo_screenwidth() / 2 - 150)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 100)}")
        # ^^^ or self.__root.eval('tk::PlaceWindow . center')
        self.__root.minsize(250, 90)
        self.title = "bar"

        self.__input_container = Frame(self.__root)
        self.__input_container.pack(fill=BOTH, expand=YES)

        self.__display_interface = Frame(self.__root)
        self.__canvas = Canvas(self.__display_interface, bg='grey')

        # window width and height
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
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
        self.__render_speed = 100
        self.finished = False

        # sorting function to run
        self.__function_to_run = func
        self.__initiator()

    def __updater(self):
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        self.__canvas_height = self.__canvas.winfo_height()
        self.__canvas_width = self.__canvas.winfo_width()
        if self.__resized and self.finished:
            print("update")
            self.draw(iter([]))
            self.__resized = False
        self.__root.after(10, self.__updater)

    def __initiator(self):
        Grid.columnconfigure(self.__input_container, 0, weight=1)
        Grid.columnconfigure(self.__input_container, 1, weight=2)
        Grid.rowconfigure(self.__input_container, 2, weight=1)

        bc_label = Label(self.__input_container, text="Bars: ")
        bc_label.grid(row=0, column=0, sticky='nsew')

        e_label = Label(self.__input_container)  # unused
        e_label.grid(row=1, column=0, columnspan=2)

        bc_entry = Entry(self.__input_container)
        bc_entry.grid(row=0, column=1, sticky='nsew')

        make = Button(self.__input_container, text="Visualize!!!", command=lambda i=0: get_data(bc_entry))
        make.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=45)

        def get_data(bc):
            try:
                self.__bar_count = int(bc.get())
            except ...:
                e_label['text'] = "Sorry, Enter Valid Number!!!"
                return
            self.__root.title(self.title)
            self.__input_container.forget()
            self.__create_bars()

        self.__updater()

    def __create_bars(self):
        self.__root.geometry(f"600x400+{int(self.__root.winfo_screenwidth() / 2 - 300)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 250)}")

        self.__render_max = self.__bar_count
        self.__display_interface.configure(bg='grey')
        self.__display_interface.pack(fill=BOTH, expand=True)

        self.__root.bind("<Configure>", self.__on_window_resize)
        self.__canvas.pack(fill=BOTH, expand=True, padx=40, pady=30)

        # adding bars to array  ----- (None for future use.. if want to add bars as widgets)
        for i in range(self.__bar_count):
            self.__bars.append((None, randrange(25,
                                                self.__canvas.winfo_reqheight()) / self.__canvas.winfo_reqheight()))

        # rendering according to function to run
        self.__canvas.after(20, self.draw, self.__function_to_run())

    def __render_bars(self, active_bars=(), b_color_set=GREY, move=False):
        self.__canvas.delete('all')

        bar_width = self.__canvas.winfo_width() / self.__bar_count
        active = list(active_bars)

        for i, bar in enumerate(self.__bars):
            # orange on remaining items
            if i < self.__render_max or len(active) == 0:
                b_color = b_color_set.split('+')[0]
            else:
                # blue on sorted
                b_color = BLUE

            if i in active:
                if i == self.__render_max - 1 and not move:
                    self.__render_max -= 1
                # green on active or reddish on swap bars
                if not move:
                    b_color = GREEN
                else:
                    b_color = b_color_set.split('+')[1]
                    # self.move_bars(*active)

            bd = self.__canvas
            bd.create_rectangle(i * bar_width + 2, bd.winfo_height() - bar[1] * bd.winfo_height(),
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
            self.__canvas.after(self.__render_speed, self.__render_bars)
            self.finished = True
            print("completed")
            return
        self.__canvas.after(self.__render_speed, self.draw, states)

    # todo implement method move_bars
    # def move_bars(self, i, j):
    #     yield
    #     x, y = j, i
    #     pass
    #     #
    #     # def update():
    #     #     return
    #     #     self.__bar_draw.after(10, update)

    def display(self):
        self.__root.mainloop()

    def set_title(self, s):
        self.title = s

    def set_render_speed(self, speed):
        self.__render_speed = speed

    def set_function_to_run(self, func, *args, **kwargs):
        self.__function_to_run = lambda i=0: func(*args, **kwargs)

    def get_bars(self):
        return self.__bars
