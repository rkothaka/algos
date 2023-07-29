import random
import uuid
from typing import List


class Interval1D:
    def __init__(self, start, end):
        if not 0 < start < end:
            raise ValueError("Invalid interval: start and end must be positive and start < end.")

        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval1D(start='{self.start}', end={self.end})"

    def __str__(self):
        return f"Interval1D: ({self.start}, {self.end})"


def create_random_interval(min_start: float = 0.0, max_end: float = 8.0, min_window: float = 0.25):
    start = round(random.uniform(min_start, max_end - min_window), 2)
    end = round(random.uniform(start+0.05, max_end), 2)
    return Interval1D(start, end)


# class Event:
#     def __init__(self, id: uuid.UUID, time: float, event_type: str):
#         self.id = id
#         self.time = time
#         self.type = event_type
#
#     def __repr__(self):
#         return f"Event(id='{self.id}', time='{self.time}', type='{self.type}')"
#
#     def __str__(self):
#         return f"Event: ({self.id}, {self.time}, {self.type})"


def find_intersecting_pairs(intervals: List[Interval1D]):
    events = []
    for interval in intervals:
        interval_id = uuid.uuid4()
        events.append((interval, interval.start, 'start'))
        events.append((interval_id, interval.end, 'end'))
    events.sort(key=lambda event: event[1])

    intersecting_pairs = []
    active_intervals = []

    for event in events:
        if event[2] == 'start':
            interval = event[0]
            active_intervals.append(interval)
            if len(active_intervals) > 1:
                intersecting_pairs.append(tuple(active_intervals))
        else:
            if interval in active_intervals:
                active_intervals.remove(interval)

    intersecting_pairs = list(set(intersecting_pairs))
    return intersecting_pairs


# Generate 6 random intervals:
n = 6
intervals = [create_random_interval() for _ in range(n)]
intersecting_pairs = find_intersecting_pairs(intervals)
for pair in intersecting_pairs:
    print(pair)
