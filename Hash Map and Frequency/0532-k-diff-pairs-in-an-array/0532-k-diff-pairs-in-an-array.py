class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counts = Counter(nums)
        count = 0

        if k == 0:
            for v in counts.values():
                if v > 1: count +=1 
        else:
            for i in counts:
                if i+k in counts: count+=1 
        
        return count