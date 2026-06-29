class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows = 1
        c_end = points[0][1]

        for s,e in points[1:]:
            if s > c_end:
                arrows +=1
                c_end = e
            
        return arrows
