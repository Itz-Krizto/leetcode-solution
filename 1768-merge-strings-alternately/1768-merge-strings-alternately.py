class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = str()
        if (len(word1)>=len(word2)):
            b = len(word2)
        else:
            b = len(word1)
        for i in range(0,b):
            a = a + word1[i]
            a = a + word2[i]
        if (len(word1)==len(word2)):
            return a
        elif (len(word1)>=len(word2)):
            for j in range(len(word2),len(word1)):
                a = a + word1[j]
            return a
        else:
            for k in range(len(word1),len(word2)):
                a = a + word2[k]
            return a