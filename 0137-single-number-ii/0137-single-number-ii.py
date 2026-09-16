class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
        
        for i in ans:
            if nums.count(i)==ans.count(i):
                return i