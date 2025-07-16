class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        matrix = [['' for _ in range(n)] for _ in range(numRows)]
        if len(s) == 1:
            return s
        else:
            row = 0
            col = 0
            curr = 0
            while (curr < n):
                while(row < numRows and curr < n):
                    matrix[row][col] = s[curr]
                    row += 1
                    curr += 1
                row = max(0,numRows-2)
                while(row > 0 and curr < n):
                    col += 1
                    matrix[row][col] = s[curr]
                    row -=1
                    curr += 1
                col += 1
            res = ''
            for i in range(numRows):
                for j in range(n):
                    res += matrix[i][j]
            return res



        