class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sP = tP = 0

        while sP < len(s) and tP < len(t):
            if s[sP] == t[tP]:
                sP+=1
            tP+=1
        
        return sP == len(s)