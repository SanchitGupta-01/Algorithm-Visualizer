from tkinter import *
from GUI.resources.colors import PALE_BLUE_LILY
from Sorting.Bubble_Sort.bubbleSort import BubbleSort


class BubbleMenu(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=14)

        self.title = 'Bubble Sort Selection'
        master.set_title(self.title)
        button_color = PALE_BLUE_LILY

        Button(self,
               text='<<<   Back To Menu   <<<',
               relief='flat',
               bg='lightgrey',
               height=1
               ).grid(row=0, column=0, sticky='nsew')

        description_labelframe = LabelFrame(self,
                                            text='Description',
                                            font='helvetica 16 bold',
                                            bg='lightgrey',
                                            # relief='flat',
                                            labelanchor='n',
                                            padx=2, pady=2)
        description_labelframe.grid(row=1, column=0, sticky='nsew')

        description_text = StringVar(description_labelframe, 'hello')

        description = Text(description_labelframe,
                           background='lightgrey',
                           width=0,
                           font='helvetica 12',
                           relief='flat',
                           state='disabled')
        description.pack(expand=True, fill=BOTH)

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
