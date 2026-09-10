class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        i = 1
        while n >= i:
            n -= i
            rows += 1
            i += 1
        return rows