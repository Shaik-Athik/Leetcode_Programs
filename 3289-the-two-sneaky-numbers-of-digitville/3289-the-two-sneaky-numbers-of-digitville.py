class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = []
        duplicates = []
        for i, v in enumerate(nums):
            if v in seen:
                duplicates.append(v)
            else:
                seen.append(v)
        
        return duplicates