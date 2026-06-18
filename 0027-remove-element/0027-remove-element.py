class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dup_finder = 0

        for i in  range(len(nums)):
            if nums[i] != val:
                nums[dup_finder] = nums[i]
                dup_finder+=1
        
        return dup_finder
