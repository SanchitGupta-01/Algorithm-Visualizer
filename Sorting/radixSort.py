from GUI.visualizers.bar import BarGUI


class RadixSort(BarGUI):
    def __init__(self, master, **kw):
        super().__init__(master,
                         lambda i=0: self.radix_sort(),
                         **kw)

    def radix_sort(self):
        pass
