import visualizers.bar as bar


class BubbleSort(bar.BarGUI):
    def __init__(self):
        super().__init__(self.bubble_sort)
        self.display()

    def bubble_sort(self):
        arr = self.get_bars()
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                print('loop')
                if arr[j][1] > arr[j+1][1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.draw((i, j), '#F87217')
                else:
                    self.draw((i, j))


BubbleSort()
