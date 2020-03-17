from tkinter import *
from GUI.menu import Menu
from GUI.controller import Controller


class Application:
    def __init__(self):
        self.running_algorithm = None
        self.__root = Tk()
        self.__root.geometry(f"900x600+{int(self.__root.winfo_screenwidth() / 2 - 450)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 350)}")

        self.interface = Menu(self, bg='grey')
        self.controller = Controller(self, bg='lightgrey')
        self.controller_button = Button(self.__root, text='<\n<\n<', width=1, bg='darkgrey', relief='flat',
                                        command=lambda i=0: self.toggle_controller())

        Grid.columnconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 1, weight=5)

        title = Label(self.__root, text='Algorithm Visualization', font='helvetica 30 bold', anchor='w',
                      bg='grey')
        title.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.interface.grid(row=1, column=0, sticky='nsew')
        self.controller_button.grid(row=1, column=1, sticky='ns')

        self.__updater()

        self.__root.mainloop()

    def __updater(self):
        if self.running_algorithm is not None:
            self.running_algorithm(self.__root).grid(row=1, column=0, rowspan=2, sticky='nsew')
            self.running_algorithm = None
        self.__root.after(10, self.__updater)

    def set_running_algorithm(self, run):
        if self.running_algorithm is None:
            self.running_algorithm = run

    def get_root(self):
        return self.__root

    def toggle_controller(self):
        if self.controller in self.__root.grid_slaves():
            self.controller.grid_forget()
            self.controller_button['text'] = '>\n>\n>'
        else:
            self.controller.grid(row=1, column=2, sticky='nsew')
            self.controller_button['text'] = '>\n>\n>'


Application()
