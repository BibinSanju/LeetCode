## Approach

use prefix sum remainder. if the same remainder appears again, the subarray between those indices has sum divisible by k. store first index of each remainder and check that length is at least 2.
TC = O(n)
SC = O(n)
