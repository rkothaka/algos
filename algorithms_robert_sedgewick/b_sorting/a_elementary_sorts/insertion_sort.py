from b_sorting.a_elementary_sorts.mysort import MySort


class InsertionSort(MySort):

    def sort(self, a):
        n = len(a)
        for i in range(1, n):
            j = i
            while j > 0 and self.less(a[j], a[j-1]):
                self.exchange(a, j, j-1)
                j -= 1
