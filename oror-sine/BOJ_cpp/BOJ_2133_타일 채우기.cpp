#include <iostream>
using namespace std;

int N, ans;
int dp[16]; 

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N;
    dp[0] = 1; dp[1] = 3;
    if (N % 2) cout << 0;
    else {
        for (int i = 2; i <= N / 2; i++)
            dp[i] = dp[i - 1] * 4 - dp[i - 2];
        cout << dp[N / 2];
    }
    return 0;
}