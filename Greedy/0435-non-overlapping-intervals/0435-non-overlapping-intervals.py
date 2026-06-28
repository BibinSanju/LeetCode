class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        c,e = 0,intervals[0][1]
        for ns, ne in intervals[1:]:
            if e > ns:
                c+=1
            else:
                e = ne
        return c
