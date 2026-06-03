class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = { 0: -1}
        cum_sum = 0

        for i, num in enumerate(nums):
            cum_sum += num
            remainder = cum_sum % k


            if remainder not in remainder_map:
                remainder_map[remainder] = i

            elif i - remainder_map[remainder] > 1:
                return True
            

        return False