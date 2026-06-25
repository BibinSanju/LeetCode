class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p1c = Counter(p)
        window = Counter(s[:len(p)])
        ans = []
        if window == p1c:
            ans.append(0)
        for i in range(len(p),len(s)):
            window[s[i]] +=1

            window[s[i-len(p)]] -=1
            if window[s[i-len(p)]] == 0:
                del window[s[i-len(p)]]
            
            if window == p1c:
                ans.append(i-len(p) + 1)
        
        return ans
