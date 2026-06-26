class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans,c = 0, 0
        sett = set("aeiou")
        for i,v in enumerate(s):
            if i>=k:
                if s[i-k] in sett:
                    c-=1
            if s[i] in sett:
                c+=1
            
            ans = max(c,ans)
        
        return ans
