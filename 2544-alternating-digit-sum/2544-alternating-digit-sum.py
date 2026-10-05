class Solution:
    def alternateDigitSum(self, n: int) -> int:
        c = int()
        for i in range(0,len(str(n))):
            c = c + ((-1)**i)*(int(str(n)[i]))
        return c