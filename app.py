from tkinter import *


class Application:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry(f"900x600+{int(self.__root.winfo_screenwidth() / 2 - 450)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 350)}")
        self.visualizer = Frame(self.__root, bg='blue')
        self.menu = Frame(self.__root, bg='yellow')
        self.controller = Frame(self.__root, bg='red')

        Grid.columnconfigure(self.__root, 0, weight=1)
        Grid.columnconfigure(self.__root, 1, weight=4)
        Grid.rowconfigure(self.__root, 0, weight=9)
        Grid.rowconfigure(self.__root, 1, weight=2)

        self.visualizer.grid(row=0, column=1, sticky='nsew')
        self.menu.grid(row=0, column=0, sticky='nsew')
        self.controller.grid(row=1, columnspan=2, sticky='nsew')

        self.__root.mainloop()


Application()
