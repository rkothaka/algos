from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class Pair:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other):
                return self.freq < other.freq or (self.freq == other.freq and self.word > other.word)

        cnt = collections.Counter(words)
        heap = []
        for word, freq in cnt.items():
            heapq.heappush(heap, Pair(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p.word for p in sorted(heap, reverse=True)]
