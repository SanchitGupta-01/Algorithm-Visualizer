from tkinter import *
from GUI.resources.colors import PALE_BLUE_LILY
from Sorting import selectionSort, radixSort, mergeSort, bubbleSort, countingSort, heapSort, quickSort, insertionSort
from Searching.A_Star.a_star import PathFinder


class Menu(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent.get_root(), *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=12)

        sort_label = Label(self, text='Sorting Algorithms', font='helvetica 20 bold',
                           bg='lightgrey').grid(row=0, column=0, sticky='nsew')

        search_label = Label(self, text='Searching Algorithms', font='helvetica 20 bold',
                             bg='lightgrey').grid(row=1, column=0, sticky='nsew')

        sorting = Frame(self, bg='darkgrey')
        sorting.grid(row=0, column=1, sticky='nsew')
        searching = Frame(self, bg='darkgrey')
        searching.grid(row=1, column=1, sticky='nsew')

        sorting.rowconfigure((0, 1, 2), weight=1)
        sorting.columnconfigure((0, 1, 2), weight=1)

        Button(sorting, text='Bubble Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(bubbleSort.BubbleSort)).grid(row=0, column=0)
        Button(sorting, text='Insertion Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(insertionSort.InsertionSort)).grid(row=0, column=1)
        Button(sorting, text='Selection Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(selectionSort.SelectionSort)).grid(row=0, column=2)
        Button(sorting, text='Merge Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(mergeSort.MergeSort)).grid(row=1, column=0)
        Button(sorting, text='Quick Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(quickSort.QuickSort)).grid(row=1, column=1)
        Button(sorting, text='Counting Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(countingSort.CountingSort)).grid(row=1, column=2)
        Button(sorting, text='Radix Sort', relief='flat', font='helvetica 15 bold', bg=PALE_BLUE_LILY,
               command=lambda i=0: parent.set_running_algorithm(radixSort.RadixSort)).grid(row=2, column=1)

        searching.rowconfigure(0, weight=1)
        searching.columnconfigure(0, weight=1)

        Button(searching, text='A* Pathfinder Algorithm', relief='flat', font='helvetica 15 bold',
               bg=PALE_BLUE_LILY, command=None).grid(row=0, column=0)  # parent.set_running_algorithm(PathFinder)
