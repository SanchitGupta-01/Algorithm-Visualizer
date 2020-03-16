import GUI.visualizers.bar as bar


class BubbleSort(bar.BarGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master, self.bubble_sort, **kwargs)

    def bubble_sort(self):
        arr = self.get_bars()
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j][1] > arr[j+1][1]:
                    yield tuple(((j, j+1), True))
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield tuple(((j, j+1), False))
                else:
                    yield tuple(((j, j+1), False))
