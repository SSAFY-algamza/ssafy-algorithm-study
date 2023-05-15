const fs = require("fs");
const readFileSync = fs.readFileSync;
const inputLines = String(readFileSync('./dev/stdin')).trim().split('\n');
const [N, M] = inputLines[0].split(' ').map(Number);
const pws = inputLines
    .slice(1, 1 + N)
    .reduce((acc, inputLine) => {
        const [k, v] = inputLine.trim().split(' ');
        acc[k] = v;
        return acc;
    }, {});

const ans = inputLines
    .slice(1 + N, 1 + N + M)
    .reduce((acc, inputLine) => acc + pws[inputLine.trim()] + '\n', "");

console.log(ans);
