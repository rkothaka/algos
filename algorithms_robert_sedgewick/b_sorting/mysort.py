from abc import ABC, abstractmethod


class MySort(ABC):
    @abstractmethod
    def sort(self, a):
        pass

    @staticmethod
    def less(i, j):
        return i < j

    @staticmethod
    def exchange(a, i, j):
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def show(a):
        arr_string = ' '.join(str(item) for item in a)
        print(arr_string)

    @staticmethod
    def sorted(a):
        return all(a[i] <= a[i+1] for i in range(len(a) - 1))
