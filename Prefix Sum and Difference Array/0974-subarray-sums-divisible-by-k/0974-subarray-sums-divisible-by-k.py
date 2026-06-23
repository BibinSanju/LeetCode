class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_map = {0: 1}
        prefix_sum , res = 0,0
        for i in nums:
            prefix_sum+=i
            rem = prefix_sum%k

            if rem in rem_map:
                res+=rem_map[rem]
                rem_map[rem] += 1
            else:
                rem_map[rem] = rem_map.get(rem,0)+1
        
        return res