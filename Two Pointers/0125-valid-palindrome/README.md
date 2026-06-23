## Approach

use left and right pointers. skip non alphanumeric chars from both sides, then compare lowercase chars. if mismatch return false, otherwise continue inward.
TC = O(n)
SC = O(1)
