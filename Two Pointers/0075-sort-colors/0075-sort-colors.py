class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0

        while i <= right:

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                i-=1
                right-=1
            i+=1
