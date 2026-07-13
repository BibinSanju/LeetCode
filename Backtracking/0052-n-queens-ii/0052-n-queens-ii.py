class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        colS, diag1, diag2 = set(), set(), set()

        def solve(row):
            nonlocal ans
            if row == n:
                ans+=1
                return
            
            for col in range(n):
                if col in colS or (row-col) in diag1 or (row+col) in diag2:
                    continue
                
                colS.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                solve(row+1)

                colS.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        
        solve(0)
        
        return ans
