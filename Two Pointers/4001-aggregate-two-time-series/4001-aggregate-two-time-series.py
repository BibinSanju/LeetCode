class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:

        all_times = sorted(set(t for t, v in series1) | set(t for t, v in series2))
        
        i, j = 0, 0
        n1, n2 = len(series1), len(series2)
        result = []
        
        for t in all_times:
            while i < n1 and series1[i][0] < t:
                i += 1
            
            while j < n2 and series2[j][0] < t:
                j += 1
            v1 = series1[i][1] if i < n1 else 0
            v2 = series2[j][1] if j < n2 else 0
            result.append([t, v1 + v2])
        return result
