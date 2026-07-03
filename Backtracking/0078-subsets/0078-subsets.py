class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(ind, path):
            if ind==len(nums):
                ans.append(path.copy())
                return
            
            path.append(nums[ind])
            backtrack(ind+1, path)
            path.pop()
            backtrack(ind+1,path)

        backtrack(0,[])
        return ans
