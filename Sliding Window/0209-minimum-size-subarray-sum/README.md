idea is, l,r pointer, r iterate from 0 -> n, if sum >= t; inner while starts to exclude left element, till the sum < t, sum-left, distance = min(ans, r - l + 1) , left +=1

TC = O(n)
SC = O(1)
