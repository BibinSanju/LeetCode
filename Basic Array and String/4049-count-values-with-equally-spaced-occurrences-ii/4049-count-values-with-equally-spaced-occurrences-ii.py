class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        lst = defaultdict(list)
        for i, val in enumerate(nums):
            lst[val].append(i)
        sc = 0
        for val, ind in lst.items():
            if len(ind) >= 3:
                
                if all(ind[j] - ind[j-1] == ind[1] - ind[0] for j in range(2,len(ind))):
                    sc+=1
        return sc
