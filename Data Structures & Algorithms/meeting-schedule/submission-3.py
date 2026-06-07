"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # (start time, end time)
        # no conflicts: no start time in between prev meeting times
        # sort by start time
        if len(intervals)==0:
            return True
        intervals.sort(key=lambda x: x.start)
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i].start<prev.end:
                return False
            prev=intervals[i]
        return True

