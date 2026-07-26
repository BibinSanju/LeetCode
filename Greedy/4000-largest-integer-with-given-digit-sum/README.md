# Intuition
To construct the largest integer with at most n digits summing to s, we should greedily place the largest possible digit (`9`) at the most significant positions (leftmost digits). Instead of looping digit by digit, we can directly determine how many full `9`s can be placed using integer division.

# Approach
1. **Edge Cases**:
   - If s = 0, the largest integer is `0`.
   - If s > 9 * n, it is impossible to reach the sum s even if all n digits are `9`, so return `-1`.

2. **Direct Calculation**:
   - Compute `q = s // 9` (the count of `9` digits) and `r = s % 9` (the remaining leftover digit).
   - If `q == n`, the entire number consists of n nines.
   - Otherwise, construct the string by concatenating q nines, the remainder digit r, and pad the rest of the positions with zeros (`n - q - 1` zeros), then convert the result to an integer.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
