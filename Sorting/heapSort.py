from GUI.visualizers.bar import BarGUI


class HeapSort(BarGUI):
    def __init__(self, master, **kw):
        super().__init__(master,
                         self.heap_sort,
                         **kw)
        self.title = 'Heap Sort Algorithm'

    def heap_sort(self):
        bars = self.get_bars()
        n = len(bars)

        def heapify(arr, heap_size, index):
            largest = index  # largest value
            left = 2 * index + 1  # left
            r = 2 * index + 2  # right

            # if left child exists
            if left < heap_size and arr[index] < arr[left]:
                largest = left

            # if right child exits
            if r < heap_size and arr[largest] < arr[r]:
                largest = r

            # root
            if largest != index:
                yield tuple(((index, 0), True))
                arr[index], arr[largest] = arr[largest], arr[index]
                yield tuple(((index, 0), False))
                # root.
                yield from heapify(arr, heap_size, largest)

        # max heap
        for i in range(n, -1, -1):
            yield from heapify(bars, n, i)

        # element extraction
        for i in range(n - 1, 0, -1):
            yield tuple(((i, 0), True))
            bars[i], bars[0] = bars[0], bars[i]  # swap
            self.add_finished_bar(i)
            yield tuple(((i, 0), False))
            yield from heapify(bars, i, 0)
