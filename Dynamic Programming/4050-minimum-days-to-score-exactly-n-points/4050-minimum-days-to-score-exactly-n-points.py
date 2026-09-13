class Solution:
    def minDays(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            k = int((math.sqrt(1 + 8 * i)-1)//2)
            if k * (k+1) //2  == i:
                dp[i] = k
                continue

            best = float('inf')
            mink = 1 if i <= 100 else max(1, k-10)

            for k in range(k, mink -1 , -1):
                t = k * (k+1) //2
                cost = k + 1 + dp[i - t]
                if cost < best:
                    best = cost
            dp[i] = best

        return dp[n]
