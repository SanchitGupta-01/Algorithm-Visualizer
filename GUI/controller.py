from tkinter import *


class Controller(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent.get_root(), *args, **kwargs)

        self.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)
        self.rowconfigure(3, weight=3)

        start = Button(self, text='Start', command=lambda i=0: parent.running_algorithm.start())
        pause = Button(self, text='Pause', command=lambda i=0: parent.running_algorithm.pause())
        stop = Button(self, text='Stop', command=lambda i=0: parent.running_algorithm.stop())

        render_frame = Frame(self, bg=self['bg'])
        render_speed = Scale(render_frame, orient=HORIZONTAL, bg=self['bg'], from_=10, to=500,
                             command=lambda i=0: parent.running_algorithm.set_render_speed(render_speed.get()))
        render_speed_label = Label(render_frame, text="Speed")

        start.grid(row=0, column=0, sticky='nsew')
        pause.grid(row=1, column=0, sticky='nsew', pady=5)
        stop.grid(row=2, column=0, sticky='nsew')

        render_frame.grid(row=3, column=0, sticky='nsew', pady=5)
        render_speed_label.grid(row=0, column=0, sticky='s')
        render_speed.grid(row=1, column=0, sticky='new')