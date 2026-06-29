class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return  [0]*n
        ans = []
        for i in range(n):
            total = 0

            if k>0:
                for j in range(1,k+1):
                    total += code[(i+j)%n]
            else:
                for j in range(1,abs(k)+1):
                    total += code[(i-j)%n]
            ans.append(total)
        
        return ans
