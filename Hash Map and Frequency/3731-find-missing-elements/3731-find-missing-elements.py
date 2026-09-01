class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minm,maxm = min(nums),max(nums)

        nums = set(nums)
        ans = []
        for i in range(minm,maxm+1):
            if i not in nums:
                ans.append(i)
        return ans
