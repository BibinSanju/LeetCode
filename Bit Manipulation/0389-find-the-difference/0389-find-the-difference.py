class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        s_sum = sum(ord(c) for c in s)
        t_sum = sum(ord(c) for c in t)

        return chr(t_sum - s_sum)
