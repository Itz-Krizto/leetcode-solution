class Solution:
    def addBinary(self, a: str, b: str) -> str:
        e = 0
        for i in range(1,len(a)+1):
            if (a[-i]) == "1":
                e = e + 2**(i-1)
        for j in range(1,len(b)+1):
            if (b[-j]) == "1":
                e = e + 2**(j-1)
        x = []
        while (e>=0):
            if (e == 0):
                x.append("0")
                break
            if (e == 1):
                x.append("1")
                break
            elif (e%2 == 1):
                x.append("1")
                e = (e - 1)//2
            else:
                x.append("0")
                e = e//2
        x.reverse()
        l = str()    
        for h in range(0,len(x)):
            l = l + x[h]
            
        return l
        