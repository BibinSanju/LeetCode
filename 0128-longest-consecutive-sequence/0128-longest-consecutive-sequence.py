class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for i in s:
            if i-1 not in s:
                current = 1

                while i + 1 in s:
                    i+=1
                    current+=1
                
                longest = max(current, longest)

        return longest