class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cum_sum = 0
        prefix_map = { 0 : 1 }

        for num in nums:
            cum_sum += num
            need = cum_sum - k
                
            ans += prefix_map.get(need, 0)
            prefix_map[cum_sum] = prefix_map.get(cum_sum, 0) + 1

        return ans