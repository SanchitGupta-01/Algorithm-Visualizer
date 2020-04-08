from tkinter import *
# from app import Application
from GUI.resources.colors import PALE_BLUE_LILY
from Sorting.Bubble_Sort.bubbleSort import BubbleSort


class BubbleMenu(Frame):

    def __init__(self, master, parent, *args, **kwargs):  # master: Application
        super().__init__(master, *args, **kwargs)
        # on interface, over main
        self.grid(row=0, column=0, sticky='nsew')

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=14)

        self.title = 'Bubble Sort Selection'
        parent.set_title(self.title)
        button_color = PALE_BLUE_LILY

        Button(self,
               text='<<<  Back  <<<',
               relief='groove',
               font='helvetica 10',
               bg='lightgrey',
               command=self.destroy
               ).grid(row=0, column=0, sticky='nsew')

        Label(self,
              text='Select Variation Of\nBubble Sort',
              font='helvetica 20 bold',
              bg='lightgrey',
              ).grid(row=1, column=0, sticky='nsew')

        algorithm_frame = Frame(self, bg='darkgrey')
        algorithm_frame.grid(row=0, column=1, rowspan=2, sticky='nsew')
        algorithm_frame.rowconfigure(0, weight=1)
        algorithm_frame.columnconfigure(0, weight=1)

        def add_buttons():
            func = parent.set_running_algorithm

            Button(algorithm_frame,
                   text='Bubble Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=button_color,
                   command=lambda i=0: func(BubbleSort)
                   ).grid(row=0, column=0, sticky='nsew')

        add_buttons()
