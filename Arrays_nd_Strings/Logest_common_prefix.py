class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minstr = float("inf")
        for str in strs:
            if len(str)<minstr:
                minstr = len(str)
        i = 0
        while i< minstr:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i+=1

        if strs[0]=='':
            return ''
        return strs[0][:i]    