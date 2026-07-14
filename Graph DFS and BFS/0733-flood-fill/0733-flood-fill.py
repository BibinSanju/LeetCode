class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        clr1 = image[sr][sc]

        if clr1 == color:
            return image

        q = deque([(sr,sc)])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            r,c = q.popleft()
            image[r][c] = color

            for dr, dc in directions:
                nx, ny = dr+r, dc+c
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and image[nx][ny] == clr1:
                    q.append((nx, ny))
        
        return image
