class Solution:
    def isPalindrome(self, x: int) -> bool:
        nor = str(x)
        rev = nor[::-1]
        if (nor == rev):
            return True
        else:
            return False