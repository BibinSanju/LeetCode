class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        count = defaultdict(int)
        ans = 0
        for a in nums1:
            for b in nums2:
                count[a+b] +=1
        for c in nums3:
            for d in nums4:
                ans+=count[-(c+d)]
        return ans