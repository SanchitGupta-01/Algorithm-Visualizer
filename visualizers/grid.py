from tkinter import *

root = Tk()
root.geometry(f"300x100+{int(root.winfo_screenwidth()/2 - 150)}+{int(root.winfo_screenheight()/2 - 100)}")
# or root.eval('tk::PlaceWindow . center')
root.minsize(250, 90)

top = Frame(root)
canvas = Canvas(root)
rows = 0
columns = 0
height = root.winfo_height()
width = root.winfo_width()
__buttons = []
title = "grid"


def set_title(s):
    global title
    title = s


def get_button():
    return __buttons


def create_grid():
    global height, width
    root.geometry(f"500x500+{int(root.winfo_screenwidth()/2 - 250)}+{int(root.winfo_screenheight()/2 - 300)}")
    root.update()
    canvas.configure(bg='grey')
    height = root.winfo_height()
    width = root.winfo_width()

    # can remove these two loops  and just set the canvas bg as black and change the padding for buttons as req.
    for j in range(0, height, int(height / columns)):
        canvas.create_line(0, j, width, j, fill='black')

    for i in range(0, width, int(width/rows)):
        canvas.create_line(i, 0, i, height, fill='black')

    set_grid()
    canvas.bind("<Configure>", on_grid_resize)
    canvas.pack(fill=BOTH, expand=True)


def on_grid_resize(e):
    global width, height
    w_scale = e.width / width
    h_scale = e.height / height
    width = e.width
    height = e.height
    canvas.scale('all', 0, 0, w_scale, h_scale)


def set_grid():
    for i in range(rows):
        bs = []
        for j in range(columns):
            button = Button(canvas, bg='grey', width=int(width / rows)+1, height=int(height / columns)+1, relief=FLAT)
            bs.append(button)
            Grid.rowconfigure(canvas, i, weight=1)
            Grid.columnconfigure(canvas, j, weight=1)
            button.bind("<Enter>", lambda e=0: e.widget.config(bg='lightgrey'))
            button.bind("<Leave>", lambda e=1: e.widget.config(bg='grey'))
            button.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')

        __buttons.append(bs)


def get_data(r, c):
    global rows, columns
    try:
        rows = int(r.get())
        columns = int(c.get())
    except ...:
        root.title("Sorry, Enter Numbers!!!")
        return
    root.title(title)
    top.forget()
    create_grid()


def initiator():
    r_label = Label(top, text="Rows: ")
    Grid.columnconfigure(top, 0, weight=1)
    Grid.columnconfigure(top, 1, weight=2)
    Grid.rowconfigure(top, 3, weight=1)
    r_entry = Entry(top)
    r_label.grid(row=0, column=0, sticky='nsew')
    r_entry.grid(row=0, column=1, sticky='nsew')
    c_label = Label(top, text="Columns: ")
    c_entry = Entry(top)
    c_label.grid(row=1, column=0, sticky='nsew')
    c_entry.grid(row=1, column=1, sticky='nsew')
    e_label = Label(top)
    e_label.grid(row=2, column=0, columnspan=2)
    make = Button(top, text="Make Grid", command=lambda i=0: get_data(r_entry, c_entry))
    make.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=45)


initiator()
top.pack(fill=BOTH, expand=YES)

root.mainloop()
