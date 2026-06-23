## Approach

store all possible sums of nums1 + nums2 in a hashmap with frequency. then for every nums3 + nums4 sum, check how many times the negative of that sum exists.
TC = O(n^2)
SC = O(n^2)
