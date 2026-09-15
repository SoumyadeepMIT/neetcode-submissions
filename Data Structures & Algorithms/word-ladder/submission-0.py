from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        n = len(wordList)
        dic = {word: [] for word in wordList}
        vis = {word: False for word in wordList}
        for i in range(n):
            for j in range(i+1, n):
                c = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k] != wordList[j][k]: c+=1
                if c==1:
                    dic[wordList[i]].append(wordList[j])
                    dic[wordList[j]].append(wordList[i])
        qu = deque()
        qu.append((beginWord, 1))
        vis[beginWord] = True
        while len(qu)>0:
            word, dis = qu.popleft()
            for nei in dic[word]:
                if nei == endWord: return dis+1
                if not vis[nei]:
                    qu.append((nei, dis+1))
                    vis[nei] = True
        return 0
