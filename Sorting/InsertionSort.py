import visualizers.bar as bar
from visualizers.colors import *


class InsertionSort(bar.BarGUI):
    def __init__(self):
        super().__init__(self.insertion_sort)
        self.display()

    def insertion_sort(self):
        arr = self.get_bars()
        n = len(arr)
        for i in range(1, n):
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                yield tuple(((j-1, j), f'{ORANGE}+{RED}', True))
                arr[j], arr[j-1] = arr[j-1], arr[j]
                yield tuple(((j-1, j), ORANGE))
                j -= 1
            else:
                yield tuple(((j-1, j), ORANGE))


InsertionSort()
