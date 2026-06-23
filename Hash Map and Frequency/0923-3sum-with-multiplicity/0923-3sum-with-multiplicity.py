class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        ans = 0

        for i, j in combinations_with_replacement(count.keys(), 2):
            k = target - i - j

            if k not in count:
                continue

            if i == j == k:
                ans += (count[i]) * (count[i]-1) * (count[i] - 2) // 6
            elif i == j != k:
                ans += count[i] * (count[i] - 1)//2 * count[k]
            
            elif k > i and k > j:
                ans += count[i] * count[j] * count[k]
            
        return ans % 1000000007