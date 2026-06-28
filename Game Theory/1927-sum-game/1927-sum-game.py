class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num)//2
        l_sum = sum(int(i) for i in num[:mid] if i.isdigit())
        r_sum = sum(int(i) for i in num[mid:] if i.isdigit())

        l_q = num[:mid].count("?")
        r_q = num[mid:].count("?")

        if (l_q + r_q) % 2 != 0:
            return True
        if 2 * (l_sum - r_sum) == (r_q - l_q) * 9:
            return False
        return True
