class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = k*threshold
        s = sum(arr[:k])
        ans = 1 if s>=threshold else 0

        for i in range(k,len(arr)):
            s += arr[i] - arr[i-k]
            ans += (s>=threshold)
        
        return ans
