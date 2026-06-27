Initially, i came up with the idea in math, like sum(1->n) - sum(nums)
this is alreay optimal, but i wanted to solve in bit manuplation too

x ^ 0 = x
x ^ x  = x

so ans = 0

then xor ans with 1->n
then xor ans with i in nums

so the missing number survives and every other cancels out

TC = O(n)
SC = O(1)
