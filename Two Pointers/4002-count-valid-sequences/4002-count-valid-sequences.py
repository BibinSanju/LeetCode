class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        total = math.comb(n-1, k-1)

        odd = math.comb((n+k-2)//2 , k-1) if (n-k)%2 == 0 else 0

        return (total - odd) % mod
