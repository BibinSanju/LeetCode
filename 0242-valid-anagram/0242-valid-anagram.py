class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for i in s:
            h2[ord(i)]+=1
        for j in t:
            h1[ord(j)]+=1
        return h1 == h2