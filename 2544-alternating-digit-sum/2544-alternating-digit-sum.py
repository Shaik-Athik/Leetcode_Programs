class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        sign = 1
        for digit in str(n):
            res += sign * int(digit)
            sign *= -1
        return res