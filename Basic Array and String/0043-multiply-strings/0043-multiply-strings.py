class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n,m = len(num1), len(num2)
        res = [0]*(n+m)
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum = res[i+j+1] + mul
                res[i+j+1] = sum % 10
                res[i+j]  += sum// 10

        ans = ''.join(map(str,res)).lstrip('0')
        return ans if ans else '0'
