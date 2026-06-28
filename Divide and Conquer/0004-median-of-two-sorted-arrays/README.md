Always binary search on the smaller array.
Partition both arrays so left side has half of total elements.
Let:Aleft, Aright
Bleft, Bright

Valid partition condition:
Aleft <= Bright and Bleft <= Aright
If valid:Odd total: median is max(Aleft, Bleft)
Even total: median is average of max(left) and min(right)

If Aleft > Bright, move left.
Else move right.

TC = O(log(min(m, n)))
SC = O(1)
