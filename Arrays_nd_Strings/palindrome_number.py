class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if the number is negative
        if x < 0:
            return False
        else:
            # the number id positive
            # now i have to reverse the number
            original = x
            rev = 0
            while x != 0:
                rev = rev*10+(x%10)
                x = x//10
        return rev == original


        