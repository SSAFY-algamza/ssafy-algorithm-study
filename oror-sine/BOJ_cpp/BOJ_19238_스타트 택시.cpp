#include<iostream>
using namespace std;
#include<queue>
#include<algorithm>

int N, M, f, grid[21][21];
struct cell { int r; int c; };
cell current;
struct passenger { cell s; cell e; } ;
passenger passengers[400];
const cell D[4] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

bool compare(const passenger &a, const passenger &b) {
	if (a.s.r != b.s.r) return a.s.r < b.s.r;
	else return a.s.c < b.s.c;
}

int get_distance(const cell& start, const cell& end) {
	if (start.r == end.r && start.c == end.c) return 0;

	queue<cell> Q; Q.push(start);
	int visited[21][21] = {};
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= N; c++) {
			visited[r][c] = grid[r][c];
		}
	}
	int distance = 0;
	while (!Q.empty()) {
		distance++;
		int qsize = Q.size();
		for (int i = 0; i < qsize; i++) {
			cell pos = Q.front(); Q.pop();
			for (int j = 0; j < 4; j++) {
				cell npos = { pos.r + D[j].r, pos.c + D[j].c };
				if (npos.r == end.r && npos.c == end.c) return distance;;
				if (1 <= npos.r && npos.r <= N && 1 <= npos.c && npos.c <= N && !visited[npos.r][npos.c]) {
					visited[npos.r][npos.c]++;
					Q.push(npos);
				}
			}
		}
	}
	return -1;
}

int drive() {
	int shortest = 400;
	int idx = -1;
	for (int i = 0; i < M; i++) {
		if (passengers[i].s.r == -1) continue;
		int distance = get_distance(current, passengers[i].s);
		if (distance == -1) continue;
		if (shortest > distance) {
			shortest = distance;
			idx = i;
		}
	}

	if (idx == -1) { f = -1; return 1; }
	if (f < shortest) { f = -1; return 1; }
	
	f -= shortest;
	shortest = get_distance(passengers[idx].s, passengers[idx].e);

	if (shortest == -1) { f = -1; return 1; }
	if (f < shortest) { f = -1; return 1; }
	
	f += shortest;
	current = passengers[idx].e;
	passengers[idx].s.r = -1;

	
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	cin >> N >> M >> f;
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= N; c++) {
			cin >> grid[r][c];
		}
	}

	cin >> current.r >> current.c;
	for (int i = 0; i < M; i++) {
		cin >> passengers[i].s.r >> passengers[i].s.c;
		cin >> passengers[i].e.r >> passengers[i].e.c;
	}

	sort(passengers, passengers + M, compare);

	for (int i = 0; i < M; i++) {
		if (drive()) break;
	}

	cout << f;

	return 0;
}