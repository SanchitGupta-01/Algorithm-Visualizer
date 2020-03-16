from GUI.visualizers.bar import BarGUI


class MergeSort(BarGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         lambda i=0: self.merge_sort(0, len(self.get_bars())),
                         **kwargs)

    def merge_sort(self, left, right):
        middle = (left + right) // 2
        if right > left:
            yield from self.merge_sort(left, middle)
            yield from self.merge_sort(middle + 1, right)

        arr = self.get_bars()
        a_1 = arr[left:middle + 1]
        a_2 = arr[middle + 1:right + 1]
        i, j, k = 0, 0, left

        while i < len(a_1) and j < len(a_2):
            if a_1[i] < a_2[j]:
                arr[k] = a_1[i]
                yield tuple(((k, i + left), True))
                i += 1
            else:
                arr[k] = a_2[j]
                yield tuple(((k, j + middle + 1), True))
                j += 1
            k += 1

        while i < len(a_1):
            arr[k] = a_1[i]
            yield tuple(((k, i + left), True))
            i += 1
            k += 1

        while j < len(a_2):
            arr[k] = a_2[j]
            yield tuple(((k, j + middle + 1), True))
            j += 1
            k += 1
