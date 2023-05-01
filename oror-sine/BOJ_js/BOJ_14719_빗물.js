// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

const max = function max(a, b) { return a > b ? a : b; };
const min = function min(a, b) { return a < b ? a : b; };

// const inputLines = String(readFileSync('input.txt')).trim().split('\n');
const inputLines = String(readFileSync('/dev/stdin')).trim().split('\n');
const [_, W] = inputLines[0].split(' ').map(Number);
const ans = inputLines[1]
  .split(' ').map(Number)
  .reduce((MHS, _, idx, IHS) => {
    if(idx === 0) return IHS.map((h) => [h, h, h]);
    MHS[idx][0] = max(MHS[idx - 1][0], IHS[idx]);
    MHS[W - 1 - idx][1] = max(MHS[W - idx][1], IHS[W - 1 - idx]);
    return MHS;
  }, null)
  .reduce((acc, _, idx, heights) => acc + min(heights[idx][0], heights[idx][1]) - heights[idx][2], 0);

console.log(ans);