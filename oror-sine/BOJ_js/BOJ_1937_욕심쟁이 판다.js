// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

const max = function max(a, b) { return a > b ? a : b; }

// let [N, ...inputLines] = String(readFileSync('input.txt')).trim().split('\n');
let [N, ...inputLines] = String(readFileSync('/dev/stdin')).trim().split('\n');
N = Number(N);
const END = N - 1;
const MAX = N * N;
const dp = Array.from({ length: MAX }, () => 0);
const origin = [];
const copy = [];
const positions = [];

inputLines.forEach((line, r) => {
  const row = line.split(' ').map(Number);
  origin.push([...row]);
  copy.push([...row]);
  row.forEach((cell, c) => positions.push([cell, r, c]));
});

const ans = positions
  .sort(([a], [b]) => b - a)
  .map(([_, r, c], idx) => {
    copy[r][c] = idx;
    return [r, c];
  })
  .reduce((acc, [r, c], idx) => {
    const UP = (r > 0 && origin[r][c] !== origin[r - 1][c]) ? copy[r - 1][c] : MAX;
    const DN = (r < END && origin[r][c] !== origin[r + 1][c]) ? copy[r + 1][c] : MAX;
    const LT = (c > 0 && origin[r][c] !== origin[r][c - 1]) ? copy[r][c - 1] : MAX;
    const RT = (c < END && origin[r][c] !== origin[r][c + 1]) ? copy[r][c + 1] : MAX;
    if (UP < idx) dp[idx] = max(dp[idx], dp[UP]);
    if (DN < idx) dp[idx] = max(dp[idx], dp[DN]);
    if (LT < idx) dp[idx] = max(dp[idx], dp[LT]);
    if (RT < idx) dp[idx] = max(dp[idx], dp[RT]);
    dp[idx] += 1;
    return max(acc, dp[idx]);
  }, 1);

console.log(ans);
