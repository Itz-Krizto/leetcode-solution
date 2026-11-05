class Solution:
    def trailingZeroes(self, n: int) -> int:
        import sys
        sys.set_int_max_str_digits(0)
        l = 1
        x = 0
        if n == 0:
            x = 0
        while n>0:
            l *= n
            n -= 1
        z = str(l)[::-1]
        for i in range(0,len(z)):
            if z[i]=='0':
                x += 1
            elif z[i]!='0':
                break
        return x
