class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        row_set = [set(matrix[r]) for r in range(n)]
        col_set = [set([matrix[j][i] for j in range(n)]) for i in range(n)]

        if any(len(i) != n for i in row_set) or any(len(i) != n for i in col_set):
            return False
        return True