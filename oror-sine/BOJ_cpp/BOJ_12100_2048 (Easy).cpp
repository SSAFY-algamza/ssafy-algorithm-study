#include <iostream>
using namespace std;

int N;
int grid[20][20][6];
int ans;

void move(int prev, int d) {
    if (prev == 5) {
        for (int r = 0; r < N; r++)
            for (int c = 0; c < N; c++)
                if (ans < grid[r][c][5]) ans = grid[r][c][5];
        return;
    }

    int cur = prev + 1;
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            grid[r][c][cur] = grid[r][c][prev];

    if (d == 0) {
        for (int c = 0; c < N; c++) {
            int merged = 0;
            for (int r = 1; r < N; r++) {
                int i = r;
                while (i >= 1 && grid[i - 1][c][cur] == 0) {
                    grid[i - 1][c][cur] = grid[i][c][cur];
                    grid[i][c][cur] = 0;
                    i--;
                }
                if (i <= merged) continue;
                if (grid[i - 1][c][cur] == grid[i][c][cur]) {
                    grid[i - 1][c][cur] *= 2;
                    grid[i][c][cur] = 0;
                    merged = i;
                }
            }
        }
    }
    else if (d == 1) {
        for (int c = 0; c < N; c++) {
            int merged = N - 1;
            for (int r = N - 2; r >= 0; r--) {
                int i = r;
                while (i <= N - 2 && grid[i + 1][c][cur] == 0) {
                    grid[i + 1][c][cur] = grid[i][c][cur];
                    grid[i][c][cur] = 0;
                    i++;
                }
                if (i >= merged) continue;
                if (grid[i + 1][c][cur] == grid[i][c][cur]) {
                    grid[i + 1][c][cur] *= 2;
                    grid[i][c][cur] = 0;
                    merged = i;
                }
            }
        }
    }
    else if (d == 2) {
        for (int r = 0; r < N; r++) {
            int merged = 0;
            for (int c = 1; c < N; c++) {
                int i = c;
                while (i >= 1 && grid[r][i - 1][cur] == 0) {
                    grid[r][i - 1][cur] = grid[r][i][cur];
                    grid[r][i][cur] = 0;
                    i--;
                }
                if (i <= merged) continue;
                if (grid[r][i - 1][cur] == grid[r][i][cur]) {
                    grid[r][i - 1][cur] *= 2;
                    grid[r][i][cur] = 0;
                    merged = i;
                }
            }
        }
    }
    else if (d == 3) {
        for (int r = 0; r < N; r++) {
            int merged = N - 1;
            for (int c = N - 2; c >= 0; c--) {
                int i = c;
                while (i <= N - 2 && grid[r][i + 1][cur] == 0) {
                    grid[r][i + 1][cur] = grid[r][i][cur];
                    grid[r][i][cur] = 0;
                    i++;
                }
                if (i >= merged) continue;
                if (grid[r][i + 1][cur] == grid[r][i][cur]) {
                    grid[r][i + 1][cur] *= 2;
                    grid[r][i][cur] = 0;
                    merged = i;
                }
            }
        }
    }
    for (int i = 0; i < 4; i++) move(cur, i);
}

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cin >> grid[r][c][0];
        }
    }
    if (N == 1) ans = grid[0][0][0];
    else for (int i = 0; i < 4; i++) move(0, i);
    cout << ans;

    return 0;
}