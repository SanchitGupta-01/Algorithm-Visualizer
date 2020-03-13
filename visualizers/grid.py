import types
from tkinter import *


class GridGUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry(f"300x100+{int(self.__root.winfo_screenwidth() / 2 - 150)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 100)}")
        # or root.eval('tk::PlaceWindow . center')
        self.__root.minsize(250, 90)
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        self.__title = "grid"

        self.__input_container = Frame(self.__root)
        self.__input_container.pack(fill=BOTH, expand=YES)

        self.__canvas = Canvas(self.__root)

        self.rows = 0
        self.columns = 0
        self.__nodes = []
        self.resized = False

        self.__initiator()

    def __updater(self):
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        if self.resized:
            self.__canvas.delete('all')
            self.__set_grid()
            self.resized = False
        self.__root.after(10 + (self.columns*self.rows)//10, self.__updater)

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

        e_label = Label(self.__input_container)  # unused error label
        e_label.grid(row=2, column=0, columnspan=2)

        make = Button(self.__input_container, text="Make Grid", command=lambda i=0: __get_data(r_entry, c_entry))
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
            self.__nodes = [['grey' for _ in range(self.columns)] for _ in range(self.rows)]
            self.__root.title(self.__title)
            self.__input_container.forget()
            self.__create_grid()
            self.add_controls()

        self.__updater()

    def __create_grid(self):
        self.__root.geometry(f"500x500+{int(self.__root.winfo_screenwidth() / 2 - 250)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 300)}")

        # can remove this (two loops) and just set the canvas bg as black and change the padding for buttons as req.
        # self.__create_lines()

        self.__canvas.after(50, self.__set_grid)
        self.__canvas.configure(bg='black')
        self.__canvas.bind("<Configure>", self.__on_grid_resize)
        self.__canvas.pack(fill=BOTH, expand=True)

    def __set_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                # button = Button(self.__canvas, bg='grey', width=int(self.width / self.rows) + 1,
                #                 height=int(self.height / self.columns) + 1, relief=FLAT,
                #                 command=lambda: self.on_button_click)
                # bs.append(button)
                # Grid.rowconfigure(self.__canvas, i, weight=1)
                # Grid.columnconfigure(self.__canvas, j, weight=1)
                # button.bind("<Enter>", lambda e=0: e.widget.config(bg='lightgrey'))
                # button.bind("<Leave>", lambda e=1: e.widget.config(bg='grey'))
                # button.grid(row=i, column=j, padx=1, pady=1, sticky='nsew')
                width = self.width / self.columns
                height = self.height / self.rows
                self.__canvas.create_rectangle(width * j, height * i, width * (j + 1), height * (i + 1),
                                               fill=self.__nodes[i][j], outline='black')

    # def __create_lines(self):
    #     for j in range(0, self.height, int(self.height / self.columns)):
    #         self.__canvas.create_line(0, j, self.width, j, fill='black')
    #
    #     for i in range(0, self.width, int(self.width / self.rows)):
    #         self.__canvas.create_line(i, 0, i, self.height, fill='black')

    def __on_grid_resize(self, e):
        # w_scale = e.width / self.width
        # h_scale = e.height / self.height
        # self.width = e.width
        # self.height = e.height
        # self.__canvas.scale('all', 0, 0, w_scale, h_scale)
        self.resized = True

    def add_controls(self):
        pass

    def set_title(self, s):
        self.__title = s

    def get_buttons(self):
        return self.__buttons

    def get_root(self):
        return self.__root

    def display(self):
        self.__root.mainloop()
    #
    # def set_button_action(self, action: types.FunctionType):
    #     self.on_button_click.__code__ = action.__code__
    #
    # @staticmethod
    # def on_button_click():
    #     pass
