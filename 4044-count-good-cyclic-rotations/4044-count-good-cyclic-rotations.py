class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2

        sum1 = sum(nums[:half])
        sum2 = sum(nums[half:])

        ans = 0 
        if sum1 > sum2:
            ans += 1

        for i in range(1,n):
            leaving_half1 = nums[i-1]
            entering_half1 = nums[(i + half - 1) % n]

            entering_half2 = nums[(i + n-1) % n]
            

            sum1 = sum1 - leaving_half1 + entering_half1
            sum2 = sum2 - entering_half1 + entering_half2

            if sum1 > sum2:
                ans += 1

        return ans