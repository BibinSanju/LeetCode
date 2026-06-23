class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, ansInd = 0, len(nums)-1, len(nums)-1

        result = [0] * len(nums)

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[ansInd] = (nums[right])**2
                right-=1
            else:
                result[ansInd] = (nums[left])**2
                left+=1
            ansInd -= 1

        return result