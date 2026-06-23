## Approach

take the expected sum from 0 to n using n * (n + 1) / 2, then subtract the actual sum of nums. whatever remains is the missing number.
TC = O(n)
SC = O(1)
