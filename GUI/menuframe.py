from tkinter import *
from GUI.resources.colors import PALE_BLUE_LILY
from Sorting.Bubble_Sort.bubbleMenu import BubbleMenu
from Sorting import selectionSort, radixSort, mergeSort, countingSort, \
    heapSort, quickSort, insertionSort, gnomeSort


class MenuFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent.get_root(), *args, **kwargs)
        self.parent = parent

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=14)

        self.button_color = PALE_BLUE_LILY

        self.main_menu()

    def main_menu(self):
        sort_label = Label(self,
                           text='Sorting Algorithms',
                           font='helvetica 20 bold',
                           bg='lightgrey')
        sorting = Frame(self, bg='darkgrey')
        search_label = Label(self,
                             text='Searching Algorithms',
                             font='helvetica 20 bold',
                             bg='lightgrey')
        searching = Frame(self, bg='darkgrey')

        sort_label.grid(row=0, column=0, sticky='nsew')
        sorting.grid(row=0, column=1, sticky='nsew')
        search_label.grid(row=1, column=0, sticky='nsew')
        searching.grid(row=1, column=1, sticky='nsew')

        def add_sorting_buttons():
            sorting.rowconfigure((0, 1, 2), weight=1)
            sorting.columnconfigure((0, 1, 2), weight=1)

            func = self.parent.set_running_algorithm

            Button(sorting,
                   text='Bubble Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(BubbleMenu.get_algorithm())
                   ).grid(row=0, column=0)
            Button(sorting,
                   text='Insertion Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(insertionSort.InsertionSort)
                   ).grid(row=0, column=1)
            Button(sorting,
                   text='Selection Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(selectionSort.SelectionSort)
                   ).grid(row=0, column=2)
            Button(sorting,
                   text='Merge Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(mergeSort.MergeSort)
                   ).grid(row=1, column=0)
            Button(sorting,
                   text='Quick Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(quickSort.QuickSort)
                   ).grid(row=1, column=1)
            Button(sorting,
                   text='Counting Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(countingSort.CountingSort)
                   ).grid(row=1, column=2)
            Button(sorting,
                   text='Heap Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(heapSort.HeapSort)
                   ).grid(row=2, column=0)
            Button(sorting,
                   text='Gnome Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(gnomeSort.GnomeSort)
                   ).grid(row=2, column=1)
            Button(sorting,
                   text='Radix Sort',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=lambda i=0: func(radixSort.RadixSort)
                   ).grid(row=2, column=2)

        add_sorting_buttons()

        def add_searching_buttons():
            searching.rowconfigure(0, weight=1)
            searching.columnconfigure(0, weight=1)

            func = self.parent.set_running_algorithm

            Button(searching,
                   text='A* Pathfinder Algorithm',
                   relief='flat',
                   font='helvetica 15 bold',
                   bg=self.button_color,
                   command=None  # func(PathFinder)
                   ).grid(row=0, column=0)

        add_searching_buttons()
