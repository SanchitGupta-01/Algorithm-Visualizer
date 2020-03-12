from tkinter import *


class GridGUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"300x100+{int(self.root.winfo_screenwidth() / 2 - 150)}"
                           f"+{int(self.root.winfo_screenheight() / 2 - 100)}")
        # or root.eval('tk::PlaceWindow . center')
        self.root.minsize(250, 90)

        self.top = Frame(self.root)
        self.canvas = Canvas(self.root)
        self.rows = 0
        self.columns = 0
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()
        self.__buttons = []
        self.title = "grid"
        self.initiator()
        self.top.pack(fill=BOTH, expand=YES)
        self.root.mainloop()

    def set_title(self, s):
        self.title = s

    def get_button(self):
        return self.__buttons

    def create_grid(self):
        self.root.geometry(f"500x500+{int(self.root.winfo_screenwidth() / 2 - 250)}"
                           f"+{int(self.root.winfo_screenheight() / 2 - 300)}")
        self.root.update()
        self.canvas.configure(bg='grey')
        self.height = self.root.winfo_height()
        self.width = self.root.winfo_width()

        # can remove these two loops  and just set the canvas bg as black and change the padding for buttons as req.
        for j in range(0, self.height, int(self.height / self.columns)):
            self.canvas.create_line(0, j, self.width, j, fill='black')

        for i in range(0, self.width, int(self.width / self.rows)):
            self.canvas.create_line(i, 0, i, self.height, fill='black')

        self.set_grid()
        self.canvas.bind("<Configure>", self.on_grid_resize)
        self.canvas.pack(fill=BOTH, expand=True)

    def on_grid_resize(self, e):
        w_scale = e.width / self.width
        h_scale = e.height / self.height
        self.width = e.width
        self.height = e.height
        self.canvas.scale('all', 0, 0, w_scale, h_scale)

    def set_grid(self):
        for i in range(self.rows):
            bs = []
            for j in range(self.columns):
                button = Button(self.canvas, bg='grey', width=int(self.width / self.rows) + 1,
                                height=int(self.height / self.columns) + 1, relief=FLAT)
                bs.append(button)
                Grid.rowconfigure(self.canvas, i, weight=1)
                Grid.columnconfigure(self.canvas, j, weight=1)
                button.bind("<Enter>", lambda e=0: e.widget.config(bg='lightgrey'))
                button.bind("<Leave>", lambda e=1: e.widget.config(bg='grey'))
                button.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')

            self.__buttons.append(bs)

    def get_data(self, r, c):
        try:
            self.rows = int(r.get())
            self.columns = int(c.get())
        except ...:
            self.root.title("Sorry, Enter Numbers!!!")
            return
        self.root.title(self.title)
        self.top.forget()
        self.create_grid()

    def initiator(self):
        r_label = Label(self.top, text="Rows: ")
        Grid.columnconfigure(self.top, 0, weight=1)
        Grid.columnconfigure(self.top, 1, weight=2)
        Grid.rowconfigure(self.top, 3, weight=1)
        r_entry = Entry(self.top)
        r_label.grid(row=0, column=0, sticky='nsew')
        r_entry.grid(row=0, column=1, sticky='nsew')
        c_label = Label(self.top, text="Columns: ")
        c_entry = Entry(self.top)
        c_label.grid(row=1, column=0, sticky='nsew')
        c_entry.grid(row=1, column=1, sticky='nsew')
        e_label = Label(self.top)
        e_label.grid(row=2, column=0, columnspan=2)
        make = Button(self.top, text="Make Grid", command=lambda i=0: self.get_data(r_entry, c_entry))
        make.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=45)


g = GridGUI()
