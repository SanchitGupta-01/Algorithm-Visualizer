from GUI.visualizers.bar import BarGUI


class GnomeSort(BarGUI):
    def __init__(self, master, **kw):
        super().__init__(master,
                         self.gnome_sort,
                         **kw)
        self.title = 'Gnome Sort Algorithm'

    def gnome_sort(self):
        index = 0
        arr = self.get_bars()

        while index < len(arr):
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                yield tuple(((index - 1, index), False))
                index = index + 1
            else:
                yield tuple(((index, index - 1), True))
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                yield tuple(((index, index - 1), False))
                index = index - 1
