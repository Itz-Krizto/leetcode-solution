class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        x = []
        for i in range(0,rowIndex+1):
            x.append([])
            for j in range(0,i+1):
                if (i!=0 and i!=1 and j!=0 and j!=i):
                    x[i].append(x[i-1][j-1] + x[i-1][j])
                else:
                    x[i].append(1)
        return x[rowIndex]