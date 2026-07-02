class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort()
        f,l = strs[0],strs[-1]
        n = min(len(f), len(l))
        for i in range(n):
            if f[i] != l[i]:
                break
            ans+=f[i]
        return ans
