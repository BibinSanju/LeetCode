class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def solve(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in col_set or (row-col) in diag1 or (row+col) in diag2:
                    continue
                
                col_set.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                board[row][col] = 'Q'

                solve(row+1)

                col_set.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
                board[row][col] = '.'



        col_set, diag1, diag2 = set(), set(), set()
        ans = []
        board = [['.'] * n for _ in range(n)]
        solve(0)

        return ans
