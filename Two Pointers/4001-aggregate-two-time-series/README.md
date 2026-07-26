# Intuition
To aggregate two sorted time series datasets, we need to sum their values at every unique timestamp that appears in either series. If a timestamp is missing in a series, its value is taken from the next available timestamp (the smallest timestamp in that series greater than or equal to the target time). If no such timestamp exists, the value is `0`. 

Instead of re-scanning the lists repeatedly for every timestamp (which causes TLE), we can use a **Two-Pointer** technique to process the sorted timestamps in linear time.

# Approach
1. **Collect Unique Timestamps**:
   - Extract all timestamps from `series1` and `series2` and sort them.

2. **Two-Pointer Traversal**:
   - Initialize two pointers `i` and `j` to `0` for `series1` and `series2` respectively.
   - Iterate through each unique timestamp `t`:
     - Advance pointer `i` forward until `series1[i][0] >= t` (the next available timestamp in `series1`).
     - Advance pointer `j` forward until `series2[j][0] >= t` (the next available timestamp in `series2`).
   - Extract `v1` from `series1[i]` (if `i < n1`, else `0`) and `v2` from `series2[j]` (if `j < n2`, else `0`).
   - Append `[t, v1 + v2]` to the result list.

3. **Why Two-Pointers?**:
   - Since `t` strictly increases, pointers `i` and `j` only move forward and never reset to `0`. This guarantees an optimal $O(N + M)$ traversal.

# Complexity
- Time complexity:
$$O((N + M) \log(N + M))$$

- Space complexity:
$$O(N + M)$$
