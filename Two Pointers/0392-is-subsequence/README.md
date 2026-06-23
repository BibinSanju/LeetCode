## Approach

use two pointers, one for s and one for t. move pointer of s only when characters match, but always move pointer of t. if s pointer reaches end, it is subsequence.
TC = O(n + m)
SC = O(1)
