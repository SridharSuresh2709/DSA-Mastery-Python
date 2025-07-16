class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        frequency_count = [0]*26
        for i in range(0,len(s)):
            index = ord(s[i]) - ord('a')
            frequency_count[index] += 1
        for i in range(0,len(t)):
            index = ord(t[i]) - ord('a')
            frequency_count[index]-=1
        if all(x == 0 for x in frequency_count):
            return True
        else:
            return False
        