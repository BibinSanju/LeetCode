class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        directions = [(0,1,'RIGHT'),(1,0,'DOWN'),(0,-1,'LEFT'),(-1,0,'UP')]
        dist = {}
        pq = [(1,0,0,True)]
        dist[(0,0,True)] = 1

        while pq:
            cost, r, c, is_odd = heapq.heappop(pq)

            if cost > dist.get((r,c,is_odd), float('inf')):
                continue

            if r == m-1 and c == n-1:
                return cost

            next_is_odd = not is_odd

            wait_cost = cost + penalty[r][c]
            if wait_cost < dist.get((r,c,next_is_odd), float('inf')):
                dist[(r, c, next_is_odd)] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, next_is_odd))

            for dr, dc, dir in directions:
                nr, nc = dr+r, dc+c

                if 0<=nr<m and 0<=nc<n:
                    n_cost = (nr+1)*(nc+1)

                    if not is_odd:
                        violate = dir in ('RIGHT', 'DOWN')
                    else:
                        violate = dir in ('LEFT', 'UP')

                    extra_cost = penalty[r][c] if violate else 0
                    move_cost = cost + n_cost + extra_cost

                    if move_cost < dist.get((nr, nc, next_is_odd), float('inf')):
                        dist[(nr,nc,next_is_odd)] = move_cost
                        heapq.heappush(pq, (move_cost,nr,nc,next_is_odd))

        return -1
