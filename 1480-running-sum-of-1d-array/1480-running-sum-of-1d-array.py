class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for ind in range(1,len(nums)):
            nums[ind] = nums[ind] + nums[ind-1]
        return nums