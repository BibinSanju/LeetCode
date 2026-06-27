Simple bit manuplation,

2^n numbers have exactly 1 set bit ie. ( 2 == 0010, 4 == 0100, 8 = 1000)

so n-1 set every other lower bits to 1  ie. 4-1 = 3 -> 0100 - 0001 = 0011

the n & (n-1) gives 0 if n is power of 2 , else any otherr value
