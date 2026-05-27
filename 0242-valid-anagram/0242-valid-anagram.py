class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = defaultdict(int)
        for i in s:
            h1[ord(i)]+=1
        for j in t:
            h1[ord(j)]-=1
        return False if any( v!=0 for k,v in h1.items()) else True