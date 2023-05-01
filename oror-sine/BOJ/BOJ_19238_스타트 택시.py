import sys
readline = sys.stdin.readline;
import heapq
from collections import deque

WALL = -1;  # 손님의 초기 위치를 1부터 지정해줄 예정
EMPTY = 0;
MAX = 22;  # 테두리를 벽으로 둘러칠 예정

N = M = fuel = taxi_r = taxi_c = 0;

grid = [[WALL]*MAX for _ in range(MAX)];
passengers = [None]*401;  # 손님의 초기 위치를 1부터 지정해줄 예정

class Passenger:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1 ;
        self.c1 = c1; 
        self.r2 = r2; 
        self.c2 = c2;


def main():
    in_put();    
    for _ in range(M):
        passenger = find_passenger();
        if passenger == -1: return print(-1);
        if transport(passenger): return print(-1);
    return print(fuel);


def in_put():
    global N, M, fuel, taxi_r, taxi_c;
    
    N, M, fuel = map(int, readline().split());
    for r in range(1, N+1):
        for c, cell in enumerate(readline().split()):
            if cell == '1': grid[r][c+1] = WALL;
            if cell == '0': grid[r][c+1] = EMPTY;

    taxi_r, taxi_c = map(int, readline().split());
    for m in range(1, M+1):
        passengers[m] = Passenger(*(int(i) for i in readline().split()));
        grid[passengers[m].r1][passengers[m].c1] = m;


dr = (-1, 0, 0, 1);
dc = (0, -1, 1, 0);
def find_passenger():
    global taxi_r, taxi_c, fuel;
    visited = [[0]*MAX for  _ in range(MAX)];
    visited[taxi_r][taxi_c] = 1
    Q = [(0, taxi_r, taxi_c)];  # 우선 순위 
    while Q:
        dist, r, c = heapq.heappop(Q);
        if dist > fuel: break;
        if grid[r][c] != WALL and grid[r][c] != EMPTY:
            fuel -= dist;
            return grid[r][c];
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i];
            if grid[nr][nc]!=WALL and visited[nr][nc] == 0:
                visited[nr][nc] = 1;
                heapq.heappush(Q, (dist+1, nr, nc));
    return -1;


def transport(idx):
    global taxi_r, taxi_c, fuel;
    visited = [[0]*MAX for  _ in range(MAX)];
    visited[passengers[idx].r1][passengers[idx].c1] = 1;
    grid[passengers[idx].r1][passengers[idx].c1] = EMPTY;
    Q = deque();
    Q.append((0, passengers[idx].r1, passengers[idx].c1));
    while Q:
        dist, r, c = Q.popleft();
        if dist > fuel: break;
        if r == passengers[idx].r2 and c == passengers[idx].c2:
            taxi_r = r; taxi_c = c; fuel += dist;
            return 0
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i];
            if grid[nr][nc]!=WALL and visited[nr][nc] == 0:
                visited[nr][nc] = 1;
                Q.append((dist+1, nr, nc));
    return 1;


if __name__== "__main__":
    main();