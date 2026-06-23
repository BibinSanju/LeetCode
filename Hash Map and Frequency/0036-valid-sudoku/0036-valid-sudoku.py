class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() #i use set because it has o(1) lookup time

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue

                row_key = (num, "row", r)
                column_key = (num, "column", c)
                box_key = (num, "box", r//3, c//3)
                
                if row_key in seen or column_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)
        
        return True