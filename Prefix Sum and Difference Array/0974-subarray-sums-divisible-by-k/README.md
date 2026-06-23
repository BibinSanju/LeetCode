## Approach

keep prefix sum remainder modulo k. if the same remainder appeared before, all those previous positions can form subarrays divisible by k with current index. store remainder counts.
TC = O(n)
SC = O(k)
