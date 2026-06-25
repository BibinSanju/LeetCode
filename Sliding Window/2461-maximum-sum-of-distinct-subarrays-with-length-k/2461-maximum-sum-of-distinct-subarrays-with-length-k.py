class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        
        window = Counter(nums[:k])
        s = 0
        c = sum(nums[:k])
        if len(window) == k:
            s = c
        for r in range(k, len(nums)):
            window[nums[r]] += 1
            c+=nums[r] - nums[r-k]
            window[nums[r-k]]-=1
            if window[nums[r-k]] == 0:
                del window[nums[r-k]]
            if len(window) == k:
                s = max(s,c)
            
        return s
