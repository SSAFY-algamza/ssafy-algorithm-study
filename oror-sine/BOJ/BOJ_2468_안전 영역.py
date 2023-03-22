import sys


def solution():
    N = int(sys.stdin.readline())
    max_height = 0
    area = []
    for _ in range(N):
        area.append([])
        for i in sys.stdin.readline().split():
            area[-1].append(int(i))
            if max_height < area[-1][-1]:
                max_height = area[-1][-1]
    ans = 1
    for h in range(1, max_height):
        visited = [[False]*N for _ in range(N)]
        cnt = 0
        for r in range(N):
            for c in range(N):
                if not visited[r][c] and area[r][c] > h:
                    cnt += 1
                    visited[r][c] = True
                    stack = [(r, c)]
                    while stack:
                        rr, cc = stack.pop()
                        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            if 0 <= (nr := rr+dr) < N and 0 <= (nc := cc+dc) < N and not visited[nr][nc]:
                                if area[nr][nc] > h:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc))
        if ans < cnt:
            ans = cnt
    return ans


print(solution())
