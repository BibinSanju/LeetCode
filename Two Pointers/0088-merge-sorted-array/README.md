## Approach

merge from the back. keep i at end of nums1 valid part, j at end of nums2, and k at last index of nums1. put bigger value at k and move pointers.
TC = O(m + n)
SC = O(1)
