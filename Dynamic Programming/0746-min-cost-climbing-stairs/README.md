## Approach

i keep dp[i] as the minimum cost to reach step i. for each step, i can come from i-1 or i-2, so dp[i] = cost[i] + min(dp[i-1], dp[i-2]). answer is min of last two steps.
TC = O(n)
SC = O(n)
