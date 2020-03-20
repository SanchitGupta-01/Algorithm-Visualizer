from GUI.visualizers.bar import BarGUI
from Sorting.countingSort import CountingSort


class RadixSort(BarGUI):
    def __init__(self, master, **kw):
        super().__init__(master,
                         lambda i=0: self.radix_sort(),
                         **kw)
        self.title = 'Radix Sort Algorithm'

    def radix_sort(self):
        CountingSort.counting_sort(self, self.get_bars())
