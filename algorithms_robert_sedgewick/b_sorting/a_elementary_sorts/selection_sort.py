from b_sorting.mysort import MySort


class SelectionSort(MySort):

    def sort(self, a):
        n = len(a)
        for i in range(n):
            low = i
            for j in range(i+1, n):
                if self.less(a[j], a[low]):
                    low = j
            self.exchange(a, i, low)
