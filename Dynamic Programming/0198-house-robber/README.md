**Idea:**
* if we skip the current house we keep the 1st previous house value
* it we take current house, we take 2nd previous ( previous of previous) + the current house

**Reccurence**

dp[i] = max( dp[i-1], dp[i-2] + current_value)

**TC** : *O(n)*
**SC**:  *O(1)*
