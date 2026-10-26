class Solution:
    def reverseWords(self, s: str) -> str:
        z = []
        x = str()
        s += " "
        for i in range(0,len(s)):
            if s[i]!=" ":
                x += s[i]    
            if s[i]==" ":
                z.append(x)
                x = str()
                continue
        y = z[::-1]
        t = []
        for i in range(0,len(y)):
            if y[i]!=str():
                t.append(y[i])       
        for i in range(0,len(t)):
            x += t[i] + " "
        return x[0:len(x)-1]



        





                
            