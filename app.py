from tkinter import *
from GUI.menuframe import MenuFrame
from GUI.controller import Controller
from GUI.visualizers.bar import BarGUI


class Application:
    def __init__(self):
        self.is_running = False
        self.run: (None, BarGUI) = None
        self.running_algorithm = None
        self.__root = Tk()
        self.__root.geometry(f"900x600+{int(self.__root.winfo_screenwidth() / 2 - 450)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 350)}")

        self.interface = MenuFrame(self, bg='grey')
        self.controller = Controller(self, bg='lightgrey')
        self.controller_button = Button(self.__root, text='<\n<\n<', width=1, bg='darkgrey', relief='flat',
                                        command=lambda i=0: self.toggle_controller())

        Grid.columnconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 1, weight=5)

        self.__title_bar = Frame(self.__root, bg='grey')
        self.__title = Label(self.__title_bar, text='Algorithm Visualization', font='helvetica 30 bold', anchor='w',
                             bg='grey')
        self.__title.pack(fill=BOTH, expand=YES, side='left')
        self.__algorithm_title = Label(self.__title_bar, text='', font='helvetica 15 bold', anchor='w',
                                       bg='grey')
        self.__title_bar.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.interface.grid(row=1, column=0, sticky='nsew')
        self.controller_button.grid(row=1, column=1, sticky='ns')

        self.__updater()

        self.__root.mainloop()

    def __updater(self):
        if self.run is not None and not self.is_running:
            self.running_algorithm = self.run(self.__root)
            self.running_algorithm.grid(row=1, column=0, rowspan=2, sticky='nsew')
            self.__algorithm_title['text'] = self.running_algorithm.title
            self.__title['text'] += '  -'
            self.__algorithm_title.pack(fill=BOTH, expand=YES, side='left')
            self.is_running = True
        self.__root.after(1, self.__updater)

    def set_running_algorithm(self, run):
        if self.run is None:
            self.run = run

    def get_root(self):
        return self.__root

    def toggle_controller(self):
        if self.controller in self.__root.grid_slaves():
            self.controller.grid_forget()
            self.controller_button['text'] = '<\n<\n<'
        else:
            self.controller.grid(row=1, column=2, sticky='nsew')
            self.controller_button['text'] = '>\n>\n>'


Application()
