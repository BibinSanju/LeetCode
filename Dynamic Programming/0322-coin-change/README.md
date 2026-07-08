**Problem Type**
Unbounded knapsack, return min number of coins, use 1d dp

**Idea**
idea is to main a dp to store the min number of coins required to make the current sum using the current amount of coins, 

**Recurence**
so when *i+coin*  is >=0 -> i) we exclude the current coins, we include the current coin , store the min of it

*Relation* -> dp[i] = min(dp[i] , 1 + dp[i-coin])

**Complexity**
TC = *O(n×amount)*
SC = *O(Amount)*
