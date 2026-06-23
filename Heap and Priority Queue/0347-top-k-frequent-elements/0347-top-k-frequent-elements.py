class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ this is my first approach, i thought to solve this'
            using heapq for o(n log k) instead of this o(n log n)
        """
        freq = Counter(nums)
        freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(freq[i][0])
        return ans # instead of this whole code, use counters.most_common()