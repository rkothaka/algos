from b_sorting.mysort import MySort


class Merge(MySort):
    aux = None

    def sort(self, a):
        def merge(lo, mid, hi):
            i, j = lo, mid + 1
            Merge.aux[lo: hi + 1] = a[lo: hi + 1]

            for k in range(lo, hi + 1):
                if i > mid:
                    a[k: hi + 1] = Merge.aux[j: hi + 1]
                    break
                elif j > hi:
                    a[k: hi + 1] = Merge.aux[i: mid + 1]
                    break
                elif self.less(Merge.aux[j], Merge.aux[i]):
                    a[k] = Merge.aux[j]
                    j += 1
                else:
                    a[k] = Merge.aux[i]
                    i += 1

        def sort_helper(lo, hi):
            if hi <= lo:
                return

            mid = lo + (hi - lo) // 2
            sort_helper(lo, mid)
            sort_helper(mid + 1, hi)
            merge(lo, mid, hi)

        Merge.aux = [None] * len(a)
        sort_helper(0, len(a) - 1)


if __name__ == "__main__":
    A = list(range(20))
    import random
    random.shuffle(A)
    print(A)
    print("After MergeSort")
    Merge.sort(A)
    print(A)
