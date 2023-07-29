from b_sorting.mysort import MySort
import random


class Quick(MySort):

    def sort(self, a):
        def partition(lo, hi):
            i, j = lo+1, hi
            item = a[lo]
            while True:
                while self.less(a[i], item):
                    if i == hi:
                        break
                    i += 1
                while self.less(item, a[j]):
                    if j == lo:
                        break
                    j -= 1
                if i >= j:
                    break
                self.exchange(a, i, j)

            self.exchange(a, lo, j)
            return j

        def sort_helper(lo, hi):
            if hi <= lo:
                return

            j = partition(lo, hi)
            sort_helper(lo, j-1)
            sort_helper(j+1, hi)

        random.shuffle(a)
        sort_helper(0, len(a) - 1)
