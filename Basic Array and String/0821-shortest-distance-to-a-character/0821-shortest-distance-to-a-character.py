class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0] * (len(s))

        prev = float('-inf')

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        
        prev = float('inf')

        for i in range(len(s)-1, -1,-1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        
        return ans