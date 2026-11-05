class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        alphanums = dict(zip(alpha,nums))
        c = columnTitle[::-1]
        x = 0
        for i in range(0,len(c)):
            x += alphanums[c[i]]*(26**i)
        return x

