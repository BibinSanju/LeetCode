class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            d[i] = d.get(i,0)+1
        for i in ransomNote:
            if i not in d or d[i] == 0:
                return False
            d[i] = d.get(i)-1

        return True
        