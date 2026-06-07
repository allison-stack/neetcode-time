"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # min heap of meeting end times
        # if curr start >= min heap top element then pop from min heap and add curr end time
        min_heap=[]
        if len(intervals)<=1:
            return len(intervals)
        intervals.sort(key=lambda x: x.start)
        for meeting in range(len(intervals)):
            if not min_heap:
                heapq.heappush(min_heap,intervals[meeting].end)
            else: 
                if intervals[meeting].start>=min_heap[0]:
                    heapq.heappop(min_heap)
                heapq.heappush(min_heap,intervals[meeting].end)
        return len(min_heap)


        
        
        