class Solution:
    def countCommas(self, n: int) -> int:
        if n>999:
            return n - 999
        elif n>9999:
            return n - 9999
        elif n>99999:
            return 2*(n - 99999)
        else:
            return 0