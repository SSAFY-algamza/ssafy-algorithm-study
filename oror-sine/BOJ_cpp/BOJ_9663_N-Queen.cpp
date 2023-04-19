#include <iostream>
using namespace std;

int N;
int row[15];
int ans;

void backtrack(int r) {
    if (r == N) {
        ans++;
        return;
    }
    for (int c = 0; c < N; c++) {

        int i = 0;
        for (; i < r; i++) {
            if (row[i] == c ) break;
            if (row[i] - i == c - r) break;
            if (row[i] + i == c + r) break;
        }

        if (i == r) {
            row[r] = c;
            backtrack(r + 1);
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    backtrack(0);
    cout << ans;
    return 0;
}