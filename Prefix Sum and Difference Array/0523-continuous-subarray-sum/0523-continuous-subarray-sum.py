class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        So, Here it is same as prefix um app. o(n), where we store the remainder as key 
        and index as val ( so using ind we can find whether the subarray has >2 elems),
        Trick is, to some subarray with rem r, we add another subarray which is mutiple ok K
        (f its multiple of K then rem == 0), we get the rem r again, so we know we added a sol, use ind diff to is it a good array, we add {0:-1}, [0,0] is a valid subarray 

        """
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