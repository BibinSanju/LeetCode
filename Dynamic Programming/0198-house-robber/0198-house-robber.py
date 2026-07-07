class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):
            skip = prev1
            take = prev2 + nums[i]

            curr = max(skip, take)

            prev2 = prev1
            prev1 = curr
        
        return curr
