from tkinter import *


class Description(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        description_labelframe = LabelFrame(self,
                                            text='Description',
                                            font='helvetica 16 bold',
                                            bg='lightgrey',
                                            labelanchor='n',
                                            padx=2, pady=2)
        description_labelframe.grid(row=0, column=0, sticky='nsew')

        description_text = StringVar(description_labelframe, 'hello')

        description = Text(description_labelframe,
                           background='lightgrey',
                           width=30,
                           height=1,
                           font='helvetica 12',
                           relief='flat',
                           state='disabled')
        description.grid(row=0, column=0)
