class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        ans = []
        count = Counter(nums1)
        for i in nums2:
            if count[i] > 0:
                ans.append(i)
                count[i] -=1
        return ans