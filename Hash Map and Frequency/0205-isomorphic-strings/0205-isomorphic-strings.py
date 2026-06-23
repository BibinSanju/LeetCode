class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t, t_s = {},{}
        for ch1,ch2 in zip(s,t):
            if ch1 in s_t:
                if s_t[ch1] != ch2:
                    return False
            else:
                s_t[ch1] = ch2
            
            if ch2 in t_s:
                if t_s[ch2] != ch1:
                    return False
            else:
                t_s[ch2] = ch1
        
        return True