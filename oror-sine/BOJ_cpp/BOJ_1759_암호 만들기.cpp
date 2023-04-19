#include <iostream>
using namespace std;
#include <algorithm>

int L, C;
char chars[15];
char ans[15];
char vowels[5] = { 'a', 'e', 'i', 'o', 'u' };

void backtrack(int depth, int idx) {
    if (idx == L) {
        int vowel_cnt = 0, consonant_cnt = 0;
        for (int i = 0; i < L; i++) {
            if (find(vowels, vowels + 5, ans[i]) != vowels + 5) vowel_cnt += 1;
            else consonant_cnt += 1;
        }
        if (vowel_cnt == 0 || consonant_cnt < 2) return;
        for (int i = 0; i < L; i++) cout << ans[i];
        cout << '\n';
        return;
    }
    if (depth == C) return;
    ans[idx] = chars[depth];
    backtrack(depth + 1, idx+1);
    backtrack(depth + 1, idx);
}

int main() {
    std::ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> L >> C;
    for (int i = 0; i < C; i++) {
        cin >> chars[i];
    }
    sort(chars, chars + C);
    backtrack(0, 0);
    return 0;
}