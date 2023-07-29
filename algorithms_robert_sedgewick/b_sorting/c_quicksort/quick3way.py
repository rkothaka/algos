from b_sorting.mysort import MySort
import random


class Quick(MySort):

    def sort(self, a):
        def sort_helper(lo, hi):
            if hi <= lo:
                return

            lt, i, gt = lo, lo+1, hi
            item = a[lo]
            while i <= gt:
                if self.less(a[i], item):
                    self.exchange(a, lt, i)
                    lt += 1
                elif self.less(item, a[i]):
                    self.exchange(a, i, gt)
                    gt -= 1

                i += 1

            sort_helper(lo, lt - 1)
            sort_helper(gt + 1, hi)

        random.shuffle(a)
        sort_helper(0, len(a) - 1)
