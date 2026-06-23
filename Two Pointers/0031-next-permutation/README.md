## Approach

from right side find the first index where nums[piv] < nums[piv+1]. swap it with the next bigger number from right side, then reverse the suffix to make it smallest possible. if no pivot exists, reverse whole array.
TC = O(n)
SC = O(1)
