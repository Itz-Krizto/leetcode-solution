class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = str()
        for x in s:
            if x.isalpha():
                z += x
            if x.isdigit():
                z += x
        z = z.lower()
        if (z == z[::-1]):
            return True
        else :
            return False
