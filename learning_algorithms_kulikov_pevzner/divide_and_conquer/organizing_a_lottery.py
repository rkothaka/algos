from collections import namedtuple
from typing import List

Event = namedtuple('Event', ('Coordinate', 'type', 'index'))


def points_cover(starts: List[float], ends: List[float], points: List[float]):
    count = [0] * len(points)

    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range(len(points)):
        events.append(Event(points[i], 'p', i))
    events = sorted(events)

    number_of_segments = 0
    for e in events:
        if e.type == 'l':
            number_of_segments += 1
        elif e.type == 'r':
            number_of_segments -= 1
        elif e.type == 'p':
            count[e.index] = number_of_segments
        else:
            assert False

    return count  # O((n + m) log(n + m))


# before(p) = # of segments that end before point p
# after(p) = # of segments that start after point p
# cover(p) = # of segments that cover p
# cover(p) = len(segments) - before(p) - after(p)

if __name__ == "__main__":
    print(points_cover([0, -3, 7], [5, 2, 10], [1, 6]))
