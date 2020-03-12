from tkinter import *
from random import randrange
import time


class BarGUI:
    def __init__(self, func):
        self.__root = Tk()
        self.__root.geometry(f"300x100+{int(self.__root.winfo_screenwidth() / 2 - 150)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 100)}")
        # or self.__root.eval('tk::PlaceWindow . center')
        self.__root.minsize(250, 90)
        self.__top = Frame(self.__root)
        self.__canvas = Canvas(self.__root)
        self.bar_count = 0
        self.__render_max = 0
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        self.bar_draw = Canvas(self.__canvas, bg='grey')
        self.__bars = []
        self.title = "bar"
        self.function_to_run = func
        self.initiator()
        self.__top.pack(fill=BOTH, expand=YES)

    def initiator(self):
        Grid.columnconfigure(self.__top, 0, weight=1)
        Grid.columnconfigure(self.__top, 1, weight=2)
        Grid.rowconfigure(self.__top, 2, weight=1)
        bc_label = Label(self.__top, text="Bars: ")
        bc_entry = Entry(self.__top)
        bc_label.grid(row=0, column=0, sticky='nsew')
        bc_entry.grid(row=0, column=1, sticky='nsew')
        e_label = Label(self.__top)  # unused
        e_label.grid(row=1, column=0, columnspan=2)
        make = Button(self.__top, text="Visualize!!!", command=lambda i=0: self.get_data(bc_entry))
        make.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=45)

    def display(self):
        self.__root.mainloop()

    def draw(self, states):
        try:
            self.__render_bars(*next(states))
        except StopIteration:
            self.bar_draw.after(300, self.__render_bars())
            print("completed")
            return
        self.bar_draw.after(300, self.draw, states)

    def set_title(self, s):
        self.title = s

    def get_bars(self):
        return self.__bars

    def get_data(self, bc):
        try:
            self.bar_count = int(bc.get())
        except ...:
            self.__root.title("Sorry, Enter Numbers!!!")
            return
        self.__root.title(self.title)
        self.__top.forget()
        self.__create_bars()

    def __create_bars(self):
        self.__root.geometry(f"600x400+{int(self.__root.winfo_screenwidth() / 2 - 300)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 250)}")
        self.__root.update()
        self.__render_max = self.bar_count
        self.__canvas.configure(bg='grey')
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()

        self.__canvas.bind("<Configure>", self.__on_window_resize)
        self.bar_draw.bind("<Configure>", self.__on_window_resize)
        self.bar_draw.pack(fill=BOTH, expand=True, padx=40, pady=30)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__canvas.update()

        # adding bars to array  ----- None for future .. if want to add bars as widgets
        for i in range(self.bar_count):
            self.__bars.append((None, randrange(50, self.__canvas.winfo_height() - 20)))

        # rendering according to function to run
        self.draw(self.function_to_run())

    def __render_bars(self, active_bars=(), b_color_set='#3D3C3A'):
        self.bar_draw.delete('all')
        bar_width = int(self.bar_draw.winfo_width() / self.bar_count)
        active = list(active_bars)
        for i, bar in enumerate(self.__bars):
            if i < self.__render_max or len(active) == 0:
                b_color = b_color_set
            else:
                b_color = '#15317E'

            if i in active:
                if i == self.__render_max-1:
                    self.__render_max -= 1
                b_color = '#6CC417'

            print(active, b_color, "render")
            bd = self.bar_draw
            bd.create_rectangle(i * bar_width + 2, bd.winfo_height() - bar[1],
                                (i + 1) * bar_width - 2, bd.winfo_height(),
                                fill=b_color, outline=b_color)

    def __on_window_resize(self, e):
        w_scale = e.width / self.width
        h_scale = e.height / self.height
        self.width = e.width
        self.height = e.height
        self.__canvas.scale('all', 0, 0, w_scale, h_scale)
