from tkinter import *

from GUI.description import Description
from GUI.menuframe import MenuFrame
from GUI.controller import Controller
from GUI.visualizers.bar import BarGUI


class Application:
    def __init__(self):
        self.is_running = False
        self.run: (None, BarGUI) = None
        self.running_algorithm: (None, BarGUI) = None
        self.__root = Tk()
        self.__root.geometry(f"900x600+"
                             f"{int(self.__root.winfo_screenwidth() / 2 - 450)}"
                             f"+{int(self.__root.winfo_screenheight() / 2 - 350)}")

        Grid.columnconfigure(self.__root, (0, 1), weight=1)
        Grid.rowconfigure(self.__root, 0, weight=1)
        Grid.rowconfigure(self.__root, 1, weight=5)

        self.__title_bar = Frame(self.__root, bg='grey')
        self.__title = Label(self.__title_bar,
                             text=' Algorithm Visualization',
                             font='helvetica 30 bold',
                             anchor='w',
                             bg='grey')
        self.__algorithm_title = Label(self.__title_bar,
                                       text='',
                                       font='helvetica 15 bold',
                                       anchor='w',
                                       bg='grey')

        self.interface = Frame(self.__root)
        self.display = Frame(self.interface)

        self.description_frame = Frame(self.interface)
        self.description = Description(self.description_frame)
        self.description_button = Button(self.description_frame,
                                         text='>\n>\n>',
                                         width=1,
                                         bg='darkgrey',
                                         relief='flat',
                                         command=lambda e=0: self.toggle_controller('description'))

        self.menu = MenuFrame(self.display, self, bg='grey')

        self.controller_frame = Frame(self.interface)
        self.controller = Controller(self.controller_frame, self, bg='lightgrey')
        self.controller_button = Button(self.controller_frame,
                                        text='<\n<\n<',
                                        width=1,
                                        bg='darkgrey',
                                        relief='flat',
                                        command=lambda e=0: self.toggle_controller('controller'))

        self.__title_bar.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.__title.pack(fill=BOTH, expand=YES, side='left')
        self.__algorithm_title.pack(fill=BOTH, expand=YES, side='left')

        self.interface.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.interface.rowconfigure(0, weight=1)
        self.interface.columnconfigure(1, weight=1)

        self.description_frame.grid(row=0, column=0, sticky='nsew')
        self.display.grid(row=0, column=1, sticky='nsew')
        self.controller_frame.grid(row=0, column=2, sticky='nsew')

        self.display.rowconfigure(0, weight=1)
        self.display.columnconfigure(0, weight=1)
        self.menu.grid(row=0, column=0, sticky='nsew')

        self.description_frame.rowconfigure(0, weight=1)
        self.controller_frame.rowconfigure(0, weight=1)
        # self.description.columnconfigure(0, weight=1)

        self.description_button.grid(row=0, column=1, sticky='ns')
        self.controller_button.grid(row=0, column=0, sticky='ns')

        def description_resize(e):
            self.description['width'] += 1
            print(self.description['width'])

        self.description_button.bind("<B1-Motion>", description_resize)

        self.__updater()

        self.__root.mainloop()

    def back_to_menu(self):
        if self.running_algorithm is not None:
            self.running_algorithm.destroy()
            self.__algorithm_title['text'] = ''
            self.__title['text'] = ' Algorithm Visualization'
            self.is_running = False

    def __updater(self):
        if self.run is not None and not self.is_running:
            self.running_algorithm = self.run(self.display)
            self.running_algorithm.grid(row=0, column=0, sticky='nsew')
            self.run = None
            self.__algorithm_title['text'] = self.running_algorithm.title
            self.__title['text'] += '  -'
            self.is_running = True

        self.__root.after(50, self.__updater)

    def set_running_algorithm(self, run):
        if self.run is None:
            self.run = run

    def set_title(self, s):
        self.__algorithm_title['text'] = s

    def get_root(self):
        return self.__root

    def toggle_controller(self, s):
        if s == 'controller':
            if self.controller in self.controller_frame.grid_slaves():
                self.controller.grid_forget()
                self.controller_button['text'] = '<\n<\n<'
            else:
                self.controller.grid(row=0, column=1, sticky='nsew')
                self.controller_button['text'] = '>\n>\n>'
        elif s == 'description':
            if self.description in self.description_frame.grid_slaves():
                self.description.grid_forget()
                self.description_button['text'] = '>\n>\n>'
            else:
                self.description.grid(row=0, column=0, sticky='nsew')
                self.description_button['text'] = '<\n<\n<'


Application()
