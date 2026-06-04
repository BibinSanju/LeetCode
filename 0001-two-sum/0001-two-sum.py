class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num  #7 2
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

    {2:0,}
   