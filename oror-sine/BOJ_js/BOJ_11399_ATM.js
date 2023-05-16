const fs = require("fs");
const readFileSync = fs.readFileSync;
const inputLines = String(readFileSync('./dev/stdin')).trim().split('\n');
const ans = inputLines[1]
    .split(' ')
    .map(Number)
    .sort((a, b) => b - a)
    .reduce((acc, value, index) => {
        return acc + value * (index + 1);
    }, 0);

console.log(ans);
