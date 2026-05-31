class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split()):
            return False

        p_s, s_p = {}, {}

        for ch1, ch2 in zip(list(pattern), list(s.split())):
            if ch1 not in p_s and ch2 not in s_p:
                p_s[ch1] = ch2
                s_p[ch2] = ch1
            elif p_s.get(ch1) != ch2 or s_p.get(ch2) != ch1:
                return False
            
        return True