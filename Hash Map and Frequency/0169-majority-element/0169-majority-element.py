class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = 0
        v = 0

        for i in nums:
            if v == 0:
                can = i
                v+=1
            elif can == i:
                v+=1
            else:
                v-=1
        
        return can
