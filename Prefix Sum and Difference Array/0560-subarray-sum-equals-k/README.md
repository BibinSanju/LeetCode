## Approach

keep running prefix sum. for current sum, if prefix_sum - k existed before, then removing that old prefix gives a subarray of sum k. hashmap stores count of each prefix sum.
TC = O(n)
SC = O(n)
