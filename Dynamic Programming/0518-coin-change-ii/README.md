**Problem Type**
Unbounded knapsack, return number of ways to make the amount, use 1D DP.

**Idea**
Maintain a dp array where:
`dp[s] = number of ways to make sum s using the coins processed so far`

**Base case:**
`dp[0] = 1`
Because there is exactly one way to make sum 0: choose no coins.

**Recurrence**
For each coin, for every current sum s:
`if s - coin >= 0:
    dp[s] += dp[s - coin]`
		
Meaning:
```
dp[s]             -> ways without using current coin newly
dp[s - coin]      -> ways to make remaining sum, then add current coin
```

**Complexity**

TC = $$O(n  * amount)$$
SC = $$O(amount)$$
