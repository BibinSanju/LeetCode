class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = float("-inf")
        ans = 0

        for num in nums:
            small = 9
            large = 0
            x = num

            if x == 0:
                small = large = 0
            
            while x > 0:
                last = x%10
                small = min(small, last)
                large = max(large, last)
                x//=10

            digit_range = large - small

            if digit_range > max_range:
                max_range = digit_range
                ans = num
            elif digit_range == max_range:
                ans+=num

        return ans
