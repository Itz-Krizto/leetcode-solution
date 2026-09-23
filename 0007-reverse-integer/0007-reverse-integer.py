class Solution:
    def reverse(self, x: int) -> int:
      if (0 <= x <= ((2**31)-1)):
        a = str(x)
        b = a[::-1]
        c = int(b)
        if (0 <= c <= ((2**31)-1)):
            return c
        else :
            return 0
      elif (-(2**31) < x <= 0):
        X = -x
        d = str(X)
        e = d[::-1]
        f = int(e)
        g = -f
        if (-(2**31) < g <= 0):
            return g
        else :
            return 0
      else:
        return 0

