class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        ans = 0

        for i in range(n):
            rotated = s[i:] + s[:i]

            score = 0
            for j in range(n-1):
                if rotated[j] == rotated[j+1]:
                    score += 1

            if score == k:
                ans += 1

        return ans