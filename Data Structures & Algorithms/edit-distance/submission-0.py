class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        n = len(word1)
        m = len(word2)
        def dist(i,j):
            if i == n:
                return m-j
            if j == m:
                return n-i
            if (i,j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dist(i+1, j+1)
            else:
                dp[(i, j)] = 1 + min([dist(i+1,j), dist(i, j+1), dist(i+1,j+1)])
            return dp[(i, j)]
        return dist(0,0)