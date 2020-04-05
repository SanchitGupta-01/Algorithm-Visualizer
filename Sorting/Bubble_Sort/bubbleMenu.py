from tkinter import *
# from app import Application
from GUI.resources.colors import PALE_BLUE_LILY
from Sorting.Bubble_Sort.bubbleSort import BubbleSort


class BubbleMenu(Frame):
    def __init__(self, master, *args, **kwargs):  # master: Application -> __root
        super().__init__(master, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=14)

        self.title = 'Bubble Sort Selection'
        master.set_title(self.title)
        button_color = PALE_BLUE_LILY

        algorithm_frame = Frame(self, bg='darkgrey')
        algorithm_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')
        algorithm_frame.rowconfigure(0, weight=1)
        algorithm_frame.columnconfigure(0, weight=1)

        def run(func):
            func(algorithm_frame).grid(row=0, column=1, rowspan=2, sticky='nsew')

        def add_buttons():
            Button(algorithm_frame,
                   text='Bubble Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=button_color,
                   command=lambda i=0: run(BubbleSort)
                   ).grid(row=0, column=0, sticky='nsew')

        add_buttons()

    @classmethod
    def get_algorithm(cls):
        pass
