import types
from tkinter import *


class GridGUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry(f"300x100+{int(self.__root.winfo_screenwidth() / 2 - 150)}"
                           f"+{int(self.__root.winfo_screenheight() / 2 - 100)}")
        # or root.eval('tk::PlaceWindow . center')
        self.__root.minsize(250, 90)

        self.__top = Frame(self.__root)
        self.__canvas = Canvas(self.__root)
        self.rows = 0
        self.columns = 0
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()
        self.__buttons = []
        self.__title = "grid"
        self._initiator()
        self.__top.pack(fill=BOTH, expand=YES)

    def set_title(self, s):
        self.__title = s

    def get_buttons(self):
        return self.__buttons

    def get_root(self):
        return self.__root

    def display(self):
        self.__root.mainloop()

    def _create_grid(self):
        self.__root.geometry(f"500x500+{int(self.__root.winfo_screenwidth() / 2 - 250)}"
                           f"+{int(self.__root.winfo_screenheight() / 2 - 300)}")
        self.__root.update()
        self.__canvas.configure(bg='grey')
        self.height = self.__root.winfo_height()
        self.width = self.__root.winfo_width()

        # can remove these two loops  and just set the canvas bg as black and change the padding for buttons as req.
        for j in range(0, self.height, int(self.height / self.columns)):
            self.__canvas.create_line(0, j, self.width, j, fill='black')

        for i in range(0, self.width, int(self.width / self.rows)):
            self.__canvas.create_line(i, 0, i, self.height, fill='black')

        self._set_grid()
        self.__canvas.bind("<Configure>", self._on_grid_resize)
        self.__canvas.pack(fill=BOTH, expand=True)

    def _on_grid_resize(self, e):
        w_scale = e.width / self.width
        h_scale = e.height / self.height
        self.width = e.width
        self.height = e.height
        self.__canvas.scale('all', 0, 0, w_scale, h_scale)

    def _set_grid(self):
        for i in range(self.rows):
            bs = []
            for j in range(self.columns):
                button = Button(self.__canvas, bg='grey', width=int(self.width / self.rows) + 1,
                                height=int(self.height / self.columns) + 1, relief=FLAT,
                                command=lambda: self.on_button_click)
                bs.append(button)
                Grid.rowconfigure(self.__canvas, i, weight=1)
                Grid.columnconfigure(self.__canvas, j, weight=1)
                button.bind("<Enter>", lambda e=0: e.widget.config(bg='lightgrey'))
                button.bind("<Leave>", lambda e=1: e.widget.config(bg='grey'))
                button.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')

            self.__buttons.append(bs)

    def _get_data(self, r, c):
        try:
            self.rows = int(r.get())
            self.columns = int(c.get())
        except ...:
            self.__root.title("Sorry, Enter Numbers!!!")
            return
        self.__root.title(self.__title)
        self.__top.forget()
        self._create_grid()

    def _initiator(self):
        r_label = Label(self.__top, text="Rows: ")
        Grid.columnconfigure(self.__top, 0, weight=1)
        Grid.columnconfigure(self.__top, 1, weight=2)
        Grid.rowconfigure(self.__top, 3, weight=1)
        r_entry = Entry(self.__top)
        r_label.grid(row=0, column=0, sticky='nsew')
        r_entry.grid(row=0, column=1, sticky='nsew')
        c_label = Label(self.__top, text="Columns: ")
        c_entry = Entry(self.__top)
        c_label.grid(row=1, column=0, sticky='nsew')
        c_entry.grid(row=1, column=1, sticky='nsew')
        e_label = Label(self.__top)
        e_label.grid(row=2, column=0, columnspan=2)
        make = Button(self.__top, text="Make Grid", command=lambda i=0: self._get_data(r_entry, c_entry))
        make.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=45)

    def set_button_action(self, action: types.FunctionType):
        self.on_button_click.__code__ = action.__code__

    @staticmethod
    def on_button_click():
        pass


g = GridGUI()
