import GUI.visualizers.bar as bar


class SelectionSort(bar.BarGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master, self.selection_sort, **kwargs)
        self.title = 'Selection Sort Algorithm'

    def selection_sort(self):
        arr = self.get_bars()
        n = len(arr)
        for i in range(n):
            min_index = i

            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
                yield tuple(((i, j, min_index), False))

            yield tuple(((i, min_index), True))
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield tuple(((i, min_index), False))
            self.add_finished_bar(i)
