const fs = require("fs");
const readFileSync = fs.readFileSync;
const inputLines = String(readFileSync('./dev/stdin')).trim().split('\n');

let [N, K] = inputLines[0].split(' ').map(Number);

let cnt = 0;
for (let i = N; i > 0; i--){
  const coin = Number(inputLines[i]);
  cnt += Math.floor(K / coin);
  K = K % coin;
  if (K == 0) break;
}

console.log(cnt);
