class Solution:
    def isPalindrome(self, s: str) -> bool:
        #raceaecar
        #race ecar

        n_str = []
        for i in s:
            if i.isalpha():
                n_str.append(i.lower())
            elif i.isdigit():
                n_str.append(i)
        
        left, right = 0, len(n_str)-1
        while left<right:
            if n_str[left] != n_str[right]:
                return False
            left+=1
            right-=1
        return True 