class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for ch in str(num):
            if num%(int(ch))==0:
                count += 1
        return count