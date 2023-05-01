// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

const sum = function sum (...args) {return args.reduce((acc, arg) => acc + arg, 0)};

// const inputLines = String(readFileSync('input.txt')).trim().split('\n');
const inputLines = String(readFileSync('/dev/stdin')).trim().split('\n');
const N = Number(inputLines[0]);
const dp = inputLines
  .slice(1).map((row) => row.trim().split(' '))
  .reduce((dp_grid, row, r) => {
    dp_grid.push(
      row.reduce((dp_row, cell, c) => {
        dp_row.push([0, 0, 0]);
        if (r === 0 && c === 1) dp_row[c][0] = 1;
        else if (cell === '1') dp_row[c][0] = -1;
        else {
          const UP = (r !== 0) ? dp_grid[r - 1][c] : [0, 0, 0];
          const LT = (c !== 0) ? dp_row[c - 1] : [0, 0, 0];
          const UL = (r !== 0 && c !== 0) ? dp_grid[r - 1][c - 1] : [0, 0, 0];
          if (UP[0] !== -1) dp_row[c][2] += UP[1] + UP[2];
          if (LT[0] !== -1) dp_row[c][0] += LT[0] + LT[1];
          if (UP[0] !== -1 && LT[0] !== -1 && UL[0] !== -1) dp_row[c][1] += UL[0] + UL[1] + UL[2];
        }
        return dp_row;
      }, [])
    )
    return dp_grid;
  }, []);
const ans = sum(...dp[N - 1][N - 1])
console.log(ans < 0 ? 0 : ans);
