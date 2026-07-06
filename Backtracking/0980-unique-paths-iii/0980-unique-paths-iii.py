class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        start_r = start_c = 0
        empty = ans = 0
        
        for r  in range(R):
            for c in range(C):
                if grid[r][c] != -1:
                    empty += 1
                if grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def backtrack(x,y,remaining):
            nonlocal ans
            if not 0<=x<R or not  0<=y<C or grid[x][y] == -1:
                return

            if grid[x][y] == 2:
                if remaining == 1:
                    ans+=1
                return
            
            grid[x][y] = -1

            for nx, ny in directions:
                backtrack(nx+x, ny+y, remaining - 1)
            grid[x][y] = 0

            return
        print(empty)
        backtrack(start_r,start_c,empty)

        return ans
