In bit manuplations, counting the set bits from 1->N has O(log N) solution (only calc the total) ,but displaying every count can be done in O(n) only.

idea is, bits[i] = bits[i>>1] + (i&1) 

if i == 5, then i // 2 == 2, (has 1 bit), i is odd , so (i&1) is 1 (101 ->1) 

if i == 6, then i//2 == 3 (has 2 bit), i is even so (i&1) is 0 (0110 -> 0)

why because bits in N (0101) must be equal to bits[N>>1] (remove last bit) + the last bit
