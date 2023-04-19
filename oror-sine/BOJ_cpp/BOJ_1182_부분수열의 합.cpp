#include <iostream>
using namespace std;

int N, S;
int seq[20];

int backtrack(int depth, int sum) {
    if (depth == N) {
        if (sum == S) return 1;
        return 0;
    }
    return backtrack(depth + 1, sum)+ backtrack(depth + 1, sum + seq[depth]);
}

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N >> S;
    for (int i = 0; i < N;i++) cin >> seq[i];
    int ans = backtrack(0, 0);
    if (S == 0) ans -= 1;
    cout << ans;
    return 0;
}