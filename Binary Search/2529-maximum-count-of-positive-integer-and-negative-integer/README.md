## Approach

since nums is sorted, i use binary search twice. first search gives the first index where value is >= 0, that is negative count. second search gives first index where value is >= 1, so n - that index is positive count. answer is max of both.
TC = O(log n)
SC = O(1)
