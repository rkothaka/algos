import collections
from typing import List


class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self) -> None:
        self._element_with_cached_max: List[Stack.ElementWithCachedMax] = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        return self._element_with_cached_max[-1].max

    def pop(self):
        return self._element_with_cached_max.pop().element

    def push(self, element):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(
                element, element if self.empty() else max(element, self.max())
            )
        )
