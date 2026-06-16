class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for i in nums:
            if i == first or i == second or i == third:
                continue
            elif i > first:
                first, second, third = i, first, second
            elif i > second:
                second, third = i, second
            elif i > third:
                third = i

        return third if (third != float('-inf')) else first