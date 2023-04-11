from collections import deque

def solution(begin, target, words):
    visited = [0] * len(words)

    def isValid(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True

    def bfs(word):
        q = deque([(word, 0)])
        while q:
            word, cnt = q.popleft()
            if word == target:
                return cnt

            for i in range(len(words)):
                if not visited[i] and isValid(word, words[i]):
                    visited[i] = 1
                    q.append((words[i], cnt + 1))
        return 0

    answer = bfs(begin)
    return answer