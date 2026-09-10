class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors_a = []
        factors_b = []
        count = 0
        
        for i in range(1,a+1):
            if a%i==0:
                factors_a.append(i)

        for i in range(1,b+1):
            if b%i==0:
                factors_b.append(i)
        
        for i in factors_a:
            if i in factors_b:
                count += 1
        
        return count