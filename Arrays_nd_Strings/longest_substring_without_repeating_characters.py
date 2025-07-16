class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {i:-1 for i in range(256)}
        l = 0
        r = 0
        maxlen = 0
        n = len(s)
        while(r < n):
            if hash[ord(s[r])] != -1:
                if hash[ord(s[r])] >= l:
                    l = hash[ord(s[r])]+1
            leng = r-l+1
            maxlen=max(leng , maxlen)
            hash[ord(s[r])] = r
            r = r+1
        return maxlen