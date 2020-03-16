import GUI.visualizers.bar as bar


class SelectionSort(bar.BarGUI):
    def __init__(self):
        super().__init__(self.selection_sort)
        self.display()

    # todo fix coloring
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


SelectionSort()
