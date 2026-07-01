class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        m = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            m = max(window[s[r]], m)

            while (r - l + 1) - m > k:
                window[s[l]]-=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
            ans = max(ans, r-l+1)
        
        return ans
