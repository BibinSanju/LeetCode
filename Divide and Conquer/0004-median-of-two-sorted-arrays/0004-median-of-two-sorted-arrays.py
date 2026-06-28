class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        half = (total+1) // 2

        left, right = 0, l1 

        while left <= right:

            mid1 = (left + right)//2 
            mid2 = half - mid1

            al = nums1[mid1-1] if mid1>0 else float("-inf")
            ar = nums1[mid1] if mid1 < l1 else float("inf")

            bl = nums2[mid2-1] if mid2 > 0 else float("-inf")
            br = nums2[mid2] if mid2 < l2 else float("inf")

            if al <= br and bl <= ar:
                if total%2 == 1:
                    return float(max(al, bl))
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                right = mid1 - 1
            else:
                left = mid1 + 1
