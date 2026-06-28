class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        ans =0
        e = float("-inf")
        for i in range(len(pairs)):
            if pairs[i][0] > e:
                e = pairs[i][1]
                ans+=1
        
        return ans
