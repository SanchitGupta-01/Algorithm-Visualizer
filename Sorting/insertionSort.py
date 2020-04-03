import GUI.visualizers.bar as bar


class InsertionSort(bar.BarGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         self.insertion_sort,
                         **kwargs)
        self.title = 'Insertion Sort Algorithm'

    def insertion_sort(self):
        arr = self.get_bars()
        n = len(arr)
        for i in range(1, n):
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                yield tuple(((j - 1, j), True))
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                if i == n - 1:
                    self.add_finished_bar(j)
                yield tuple(((j - 1, j), False))
                j -= 1

            else:
                yield tuple(((j-1, j), False))
