class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = 0
        for i in range(1,len(s)+1):
            if (i != 1):
                if (((s[-i+1]) != " ") and ((s[-i]) == " ")):
                    break
                elif (s[-i] == " "):
                    continue
                elif (s[-i] != " "):
                    a = a + 1
            else:
                if (s[-1] == " "):
                    continue
                elif (s[-1] != " "):
                    a = a + 1
        return a  
