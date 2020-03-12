from tkinter import *

root = Tk()
root.geometry(f"300x100+{int(root.winfo_screenwidth()/2 - 150)}+{int(root.winfo_screenheight()/2 - 100)}")
# or root.eval('tk::PlaceWindow . center')
root.minsize(250, 90)

top = Frame(root)
rows = 0
columns = 0
title = "grid"


def set_title(s):
    global title
    title = s


def create_grid():
    canvas = Canvas(root)
    root.geometry(f"500x500+{int(root.winfo_screenwidth()/2 - 250)}+{int(root.winfo_screenheight()/2 - 300)}")
    root.update()
    height = root.winfo_height()
    width = root.winfo_width()
    for j in range(0, height, int(height / columns)):
        canvas.create_line(0, j, width, j, fill='black')

    for i in range(0, width, int(width/rows)):
        canvas.create_line(i, 0, i, height, fill='black')

    canvas.pack(fill=BOTH, expand=True)


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
    map(button_config, [])


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
