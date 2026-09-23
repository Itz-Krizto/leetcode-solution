class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = 0
        digits.reverse()
        for i in range(0,len(digits)):
            a = (digits[i])*(10**i)
            l = l + a
        b = l + 1
        c = str(b)
        d = []
        for z in range(0,len(c)):
            d.append(c[z])
        for x in range(0,len(d)):
            d[x] = int(d[x])
        return d
            
            





