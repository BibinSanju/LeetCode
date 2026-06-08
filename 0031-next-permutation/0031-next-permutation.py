class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        piv = n-2

        while piv >= 0 and nums[piv] >= nums[piv+1]:
            piv-=1
        
        if piv >= 0:
            right = n-1

            while nums[right] <= nums[piv]:
                right -= 1
            
            nums[piv], nums[right] = nums[right], nums[piv]

        l = piv + 1
        r = n-1

        while l < r:
            nums[l], nums[r] = nums[r],nums[l]
            l+=1
            r-=1