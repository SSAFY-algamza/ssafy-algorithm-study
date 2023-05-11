// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

// const N = Number(readFileSync('input.txt'));
const N = Number(readFileSync('/dev/stdin'));

let ans = 0;
let divisor = 5;

while (divisor <= N) {
  ans += Math.floor(N / divisor);
  divisor *= 5;
}

console.log(ans);
