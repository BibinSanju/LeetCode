class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            not a big deal, so for o(n) time, I look from a index i, is there some 
            portion or subarray from 0 to i , I can chop off to achive the target subarray,
            so i store prefix sum (counts), so when I stand in index i, i how the count  of 
            subarray (who has a sum i need to chop to get k), there may be many subarray with 
            same value (i.e 1), I can chop , so I gets the total sub array which will be == 
            the count of prefix sum i delete
        """
        ans = 0
        cum_sum = 0
        prefix_map = { 0 : 1 }

        for num in nums:
            cum_sum += num
            need = cum_sum - k
                
            ans += prefix_map.get(need, 0)
            prefix_map[cum_sum] = prefix_map.get(cum_sum, 0) + 1

        return ans