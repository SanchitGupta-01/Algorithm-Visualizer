from GUI.visualizers.bar import BarGUI


class CountingSort(BarGUI):
    def __init__(self, master, **kw):
        super().__init__(master,
                         lambda i=0: self.counting_sort(),
                         **kw)

    def counting_sort(self):
        bars = self.get_bars()
        count_dict = dict([(bar, 0) for bar in bars])

        for i, num in enumerate(bars):
            count_dict[num] += 1
            yield tuple((tuple([i]), False))

        prev = None
        b = list(set(bars.copy()))
        b.sort()
        for num in b:
            if prev:
                count_dict[num] += count_dict[prev]
            prev = num

        for num in bars.copy():
            count_dict[num] -= 1
            print(count_dict[num])
            bars[count_dict[num]] = num
            yield tuple((tuple([count_dict[num]]), True))
            self.add_finished_bar(count_dict[num])
