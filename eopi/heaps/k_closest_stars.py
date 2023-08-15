import math
from typing import Iterator, List, Tuple
import heapq


class Star:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 +self.z**2)

    def __lt__(self, other: 'Star') -> bool:
        return self.distance < other.distance


def find_closest_k_start(stars: Iterator[Star], k: int) -> List[Star]:
    max_heap: List[Tuple[float, Star]] = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    return [s[1] for s in heapq.nlargest(k, max_heap)]
