class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                if isPali(left+1,right) or isPali(left, right-1):
                    return True
                else:
                    return False
            left+=1
            right-=1
        return True