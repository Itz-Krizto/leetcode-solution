class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        x = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if len(digits)==1:
            return x[digits]
        if len(digits)==2:
            a = []
            for i in range(0,len(x[digits[0]])):
                for j in range(0,len(x[digits[1]])):
                    a.append(x[digits[0]][i]+x[digits[1]][j])
            return a
        if len(digits)==3:
            a = []
            for i in range(0,len(x[digits[0]])):
                for j in range(0,len(x[digits[1]])):
                    for k in range(0,len(x[digits[2]])):
                        a.append(x[digits[0]][i]+x[digits[1]][j]+x[digits[2]][k])
            return a
        if len(digits)==4:
            a = []
            for i in range(0,len(x[digits[0]])):
                for j in range(0,len(x[digits[1]])):
                    for k in range(0,len(x[digits[2]])):
                        for l in range(0,len(x[digits[3]])):
                            a.append(x[digits[0]][i]+x[digits[1]][j]+x[digits[2]][k]+x[digits[3]][l])
            return a