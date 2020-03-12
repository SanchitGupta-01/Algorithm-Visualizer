from tkinter import *
from random import randrange


class BarGUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry(f"300x100+{int(self.__root.winfo_screenwidth() / 2 - 150)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 100)}")
        # or self.__root.eval('tk::PlaceWindow . center')
        self.__root.minsize(250, 90)

        self.__top = Frame(self.__root)
        self.__canvas = Canvas(self.__root)
        self.bar_count = 0
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        self.bar_draw = Canvas(self.__canvas, bg='grey')
        self.__bars = []
        self.title = "bar"
        self.initiator()
        self.__top.pack(fill=BOTH, expand=YES)
        self.__root.mainloop()

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
        self.create_bars()

    def create_bars(self):
        self.__root.geometry(f"600x400+{int(self.__root.winfo_screenwidth() / 2 - 300)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 250)}")
        self.__root.update()
        self.__canvas.configure(bg='grey')
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()

        self.__canvas.bind("<Configure>", self.on_window_resize)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__canvas.update()

        # adding bars to array  ----- None for future .. if want to add bars as widgets
        for i in range(self.bar_count):
            self.__bars.append((None, randrange(50, self.__canvas.winfo_height()-20)))

        # rendering bars
        self.render_bars()

    def render_bars(self):
        self.bar_draw.pack(fill=BOTH, expand=True, padx=40, pady=30)
        self.bar_draw.update()
        bar_width = int(self.bar_draw.winfo_width() / self.bar_count)
        for i, bar in enumerate(self.__bars):
            with self.bar_draw as bd:
                bd.create_rectangle(i * bar_width + 2, bd.winfo_height() - bar[1],
                                    (i+1)*bar_width - 2, bd.winfo_height(), fill='#3D3C3A', outline='#3D3C3A')

    def on_window_resize(self, e):
        w_scale = e.width / self.width
        h_scale = e.height / self.height
        self.width = e.width
        self.height = e.height
        self.__canvas.scale('all', 0, 0, w_scale, h_scale)


BarGUI()
