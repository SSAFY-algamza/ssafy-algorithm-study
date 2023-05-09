from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
switches = [[[] for _ in range(N)] for _ in range(N)]
rooms = [[0]*N for _ in range(N)]
rooms[0][0] = 1

for _ in range(M):
    x, y, a, b = map(int, input().split())
    switches[x-1][y-1].append((a-1, b-1))



# 방마다 이동 가능한 칸 리스트에 추가
# 불이 안켜져서 못갔던 칸 저장하는 리스트 invalid_room 만들기
# 불을 켤때마다 invalid_room에 있는 방인지 확인 -> 맞으면 그 방 이동해서 불켜고 이동 가능한 방 리스트 추가
delta = [(1,0),(-1,0),(0,1),(0,-1)]
possible_rooms = deque([(0,0)])
invalid_rooms = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
while possible_rooms:
    x, y = possible_rooms.popleft()
    visited[x][y] = 1
    for px, py in switches[x][y]:
        rooms[px][py] = 1
        if invalid_rooms[px][py] and not visited[px][py]:
            invalid_rooms[px][py] = 0
            possible_rooms.append((px,py))
    for dx, dy in delta:
        nx, ny = dx+x, dy+y
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if rooms[nx][ny]:
                possible_rooms.append((nx,ny))
            else:
                invalid_rooms[nx][ny] = 1

ans = sum([sum(room) for room in rooms])
print(ans)

# for r in rooms:
#     print(*r)

'''
4 10
1 1 1 2
1 2 1 3
1 2 4 1
1 3 1 4
1 3 3 1
1 4 2 4
1 4 2 1
2 1 4 4
3 1 4 3
4 1 3 4
'''