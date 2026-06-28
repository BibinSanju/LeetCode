# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            g = (l+r)//2
            op = guess(g)
            if not op:
                return g
            elif op == 1:
                l = g+1
            else:
                r = g-1
