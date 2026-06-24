class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1c = Counter(s1)
        window = {}
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i],0) + 1
        if s1c == window:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1

            window[s2[i-len(s1)]]-=1
            if window[s2[i-len(s1)]] == 0:
                del window[s2[i-len(s1)]]

            if window == s1c:
                return True
        return False
