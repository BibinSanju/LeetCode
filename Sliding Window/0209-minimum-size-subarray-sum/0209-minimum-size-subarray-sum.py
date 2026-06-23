class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        c_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            c_sum += nums[right]

            while c_sum >= target:
                ans = min(ans, right - left +1)
                c_sum -= nums[left]
                left+=1
        
        return ans if ans != float('inf') else 0
