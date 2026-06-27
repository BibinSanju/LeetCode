class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, m = 0, 1
        basket = Counter(fruits[:1])

        for r in range(1,len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]]-=1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l+=1
            
            m = max(m, r-l+1)
        return m
