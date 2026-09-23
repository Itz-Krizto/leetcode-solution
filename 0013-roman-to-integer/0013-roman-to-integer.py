class Solution:
    def romanToInt(self, s: str) -> int:
        sum = (1*s.count("I")) + (5*s.count("V")) + (10*s.count("X")) + (50*s.count("L")) + (100*s.count("C")) + (500*s.count("D")) + (1000*s.count("M"))
        if (s.count("IV")==1):
            sum = sum - 2
        if (s.count("IX")==1):
            sum = sum - 2
        if (s.count("XL")==1):
            sum = sum - 20
        if (s.count("XC")==1):
            sum = sum - 20
        if (s.count("CD")==1):
            sum = sum - 200
        if (s.count("CM")==1):
            sum = sum - 200
            return sum
        else:
            return sum