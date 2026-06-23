## Approach

use xor for all numbers. same numbers cancel out because x ^ x = 0, and 0 ^ num = num, so finally only the single number remains.
TC = O(n)
SC = O(1)
