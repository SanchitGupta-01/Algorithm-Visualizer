from GUI.visualizers.bar import BarGUI


class QuickSort(BarGUI):
    def __init__(self):
        super().__init__(lambda i=0: self.quick_sort(0, len(self.get_bars())))
        self.set_render_speed(1)
        self.display()

    def quick_sort(self, left, right):
        if right > left:
            arr = self.get_bars()
            i = left - 1
            print(i, left, right, " ", )
            for j in range(left, right - 1):
                if arr[j] < arr[right - 1]:
                    i += 1
                    yield tuple(((i, right - 1), True))
                    arr[i], arr[j] = arr[j], arr[i]
                    yield tuple(((i, right - 1), False))
                else:
                    yield tuple(((i, right - 1), False))

            print(i+1, right - 1)
            arr[i + 1], arr[right - 1] = arr[right - 1], arr[i + 1]

            yield from self.quick_sort(left, i + 1)
            yield from self.quick_sort(i + 2, right)


QuickSort()
