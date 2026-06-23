class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        def BS(t):
            l,r = 0,n

            while l < r:
                mid = (l+r)//2
                if nums[mid] < t:
                    l = mid+1
                else:
                    r = mid
                
            return l


        negative_pos = BS(0)
        positive_pos = n-BS(1)

        return max(negative_pos, positive_pos)