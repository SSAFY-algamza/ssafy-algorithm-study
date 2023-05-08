// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

// const [M, N] = String(readFileSync('input.txt')).trim().split(' ').map(Number);
const [M, N] = String(readFileSync('/dev/stdin')).trim().split(' ').map(Number);
const numbers = Array.from({length:N+1}, (_, k)=> k);
numbers[1] = 0;
for (let i = 2; i <= N; i++){
  if (numbers[i] === 0) continue;
  for (let j = 2*i; j <= N; j+=i) {
    numbers[j] = 0;
  }
}

console.log(numbers.filter((v, i)=> i >= M && v).join('\n'));
