class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort()

        def add_p(result,x,h):
            if result and result[-1][-1] == h:
                return
            if result and result[-1][0] == x:
                result[-1] = (x, max(result[-1][-1], h))
                return
            result.append((x,h))

        def merge(l_arr, r_arr):
            result = []
            h1, h2 = 0,0
            l1, l2 = len(l_arr), len(r_arr)
            l,r = 0,0

            while l < l1 and r < l2:
                x1, y1 = l_arr[l]
                x2, y2 = r_arr[r]

                if x1 < x2:
                    x = x1
                    h1 = y1
                    l+=1
                elif x1 > x2:
                    x = x2
                    h2 = y2
                    r+=1
                else:
                    x = x1
                    h1 = y1
                    h2 = y2
                    l+=1
                    r+=1
                
                h = max(h1, h2)
                add_p(result,x,h)

            while l < l1:
                x1, y1 = l_arr[l]
                add_p(result,x1,y1)
                l+=1
            while r < l2:
                x2,y2 = r_arr[r]
                add_p(result, x2, y2)
                r+=1
            
            return result



        def solve(arr):
            if len(arr) == 1:
                l,r,h = arr[0]
                return [(l,h),(r,0)]
            mid = len(arr) // 2
            l_arr = solve(arr[:mid])
            r_arr = solve(arr[mid:])

            return merge(l_arr, r_arr)


        return solve(buildings)
