class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # break ito positive and negative block seperatly
        x = str(x)
        negative = False
        if x[0] == '-':
            negative = True
            x = x[1:]
        x = x[::-1]
        x = int(x)
        if negative:
            x = -x
        if -2**31 <= x <= ((2**31)-1):
            return x
        else:
            return 0