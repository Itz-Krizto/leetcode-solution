class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n>=1):
            while (n>=1):
                if ((n>1) and (n%2==0)):
                    n = n/2
                elif (n==1):
                    return True
                else:
                    return False
        elif (0<n<=1):
            while ():
                if (n<=1):
                    n = n*2
                elif (n==1):
                    return True
                else:
                    return False 
        else:
            return False