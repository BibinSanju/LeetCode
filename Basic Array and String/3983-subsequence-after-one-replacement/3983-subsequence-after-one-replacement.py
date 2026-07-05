class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        n = len(s)
        change = normal = 0

        for ch in t:
            old_change = change
            old_normal = normal

            if old_change < n and s[old_change] == ch:
                change = max(change, old_change+1)

            if old_normal < n:
                change = max(change, old_normal+1)

            if old_normal < n and s[old_normal] == ch:
                normal+=1

            if change == n or normal == n:
                return True

        return False
