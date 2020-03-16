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
        self.controller = Controller(self.__root, bg='blue')

        Grid.columnconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 1, weight=16)
        Grid.rowconfigure(self.__root, 2, weight=16)

        title = Label(self.__root, text='Algorithm Visualization', font='helvetica 30 bold', anchor='sw',
                      bg='grey')
        title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.interface.grid(row=1, column=0, rowspan=2, sticky='nsew')
        # self.controller.grid(row=3, column=0, sticky='nsew')

        self.__updater()

        self.__root.mainloop()

    def __updater(self):
        if self.running_algorithm is not None:
            self.running_algorithm(self.__root).grid(row=1, column=0, rowspan=2, sticky='nsew')
            self.running_algorithm = None
        self.__root.after(100, self.__updater)

    def set_running_algorithm(self, run):
        if self.running_algorithm is None:
            self.running_algorithm = run

    def get_root(self):
        return self.__root


Application()
