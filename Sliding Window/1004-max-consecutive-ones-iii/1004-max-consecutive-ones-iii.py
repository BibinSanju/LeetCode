class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m,l, z_count = 0,0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                z_count+=1
            
            while z_count > k:
                if nums[l] == 0:
                    z_count-=1
                l+=1
        
            m = max(m, r-l+1)
        
        return m
