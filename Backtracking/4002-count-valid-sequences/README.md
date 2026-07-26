# Intuition
A sequence's product is **even** if **at least one** integer in the sequence is even. 

Instead of directly counting sequences with at least one even integer, we use **Complementary Counting**:
$$\text{Valid Sequences} = (\text{Total Sequences}) - (\text{All-Odd Sequences})$$

Both parts can be solved efficiently using **Stars and Bars**:
1. **Total Sequences**: The number of ways to partition $n$ into $k$ positive integers is given by $\binom{n - 1}{k - 1}$.
2. **All-Odd Sequences**: Writing each odd integer as $a_i = 2x_i + 1$ (where $x_i \ge 0$), the sum equation simplifies to $x_1 + x_2 + \dots + x_k = \frac{n - k}{2} = m$.
   - If $(n - k)$ is odd or $n < k$, no odd sequence can sum to $n \implies \text{Odd} = 0$.
   - If $(n - k)$ is even, the number of non-negative integer solutions is $\binom{m + k - 1}{k - 1}$.

# Approach
1. **Base Case**: If $n < k$, return `0`.
2. Compute $\text{Total} = \binom{n - 1}{k - 1} \pmod{10^9 + 7}$.
3. If $(n - k)$ is even, set $m = (n - k) // 2$ and compute $\text{Odd} = \binom{m + k - 1}{k - 1} \pmod{10^9 + 7}$, otherwise $\text{Odd} = 0$.
4. Return $(\text{Total} - \text{Odd}) \pmod{10^9 + 7}$.

# Complexity
- Time complexity:
$$O(k)$$

- Space complexity:
$$O(1)$$
