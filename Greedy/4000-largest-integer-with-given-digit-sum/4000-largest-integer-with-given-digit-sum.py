class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
            
        if s > 9*n:
            return -1
            
        q = s // 9
        r = s % 9

        if q == n:
            return int ('9' * q)

        return int( ('9' * q) + str(r) + ('0' * ( n - q - 1)) )
