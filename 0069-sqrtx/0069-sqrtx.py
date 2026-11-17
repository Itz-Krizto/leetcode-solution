class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        n = 0
        a = 0
        while i>=0:
            a = a + 1
            n = n + i
            i = i + 2
            if n>x:
                return (a-1)
                break
            elif n==x:
                return (a)
                break



