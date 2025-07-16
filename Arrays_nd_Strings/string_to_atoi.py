class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #  +1337c0d3
        # remove leading whitespace
        s = s.strip(' ') # +1337c0d3
        if len(s) == 0:
            return 0
        index = 0
        result = 0
        sign = 1
        if s[index] == '+' or s[index] == '-':
            if s[index] == '-':
                sign = -1
            index += 1
        while index < len(s) and s[index].isdigit():
            result = result*10 + int(s[index])
            index += 1
        if sign == -1:
            result = result*sign
        if result < -2**31:
            return -2**31
        elif result > ((2**31) - 1):
            return 2**31-1
        else:
            return result
        



        

        