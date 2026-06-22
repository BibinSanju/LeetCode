class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win_set = set()
        l, ans = 0,0

        for r in range(len(s)):
            while s[r] in win_set:
                win_set.remove(s[l])
                l+=1
            win_set.add(s[r])
            ans = max(ans, r-l+1)
        
        return ans
