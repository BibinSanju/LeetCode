class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        lst = defaultdict(list)
        for i, val in enumerate(nums):
            lst[val].append(i)
        sc = 0
        for val, ind in lst.items():
            if len(ind) == 3:
                if ind[2] - ind[1] == ind[1] - ind[0]:
                    sc+=1
        return sc
