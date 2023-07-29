from b_sorting.mysort import MySort


class ShellSort(MySort):

    def sort(self, a):
        n = len(a)

        h = 1
        while h < n//3:
            h = 3*h + 1

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and self.less(a[j], a[j-h]):
                    self.exchange(a, j, j-h)
                    j -= h

            h //= 3
