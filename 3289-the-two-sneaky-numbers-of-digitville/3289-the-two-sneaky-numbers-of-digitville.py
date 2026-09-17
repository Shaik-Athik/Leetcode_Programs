class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if nums.count(x) == 2:
                if x not in ans:
                    ans.append(x)
        
        return ans
