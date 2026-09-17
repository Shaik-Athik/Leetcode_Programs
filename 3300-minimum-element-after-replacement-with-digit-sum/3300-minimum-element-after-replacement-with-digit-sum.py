class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumofdigits(num: int) -> int:
            s = str(num)
            n = 0
            for ch in s:
                n += int(ch)
            return n
        
        ans = []
        for num in nums:
            ans.append(sumofdigits(num))
        
        return min(ans)