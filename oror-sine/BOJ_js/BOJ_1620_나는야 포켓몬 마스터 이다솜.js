// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

// const inputLines = String(readFileSync('input.txt')).trim().split('\n');
const inputLines = String(readFileSync('/dev/stdin')).trim().split('\n');

const [N, M] = inputLines[0].split(' ').map(Number);

const dictionary = inputLines.slice(1, 1 + N).reduce((acc, pokemon, index) => {
  acc[pokemon.trim()] = index + 1;
  return acc;
}, {});

const ans = inputLines.slice(1 + N, 1 + N + M).map((query) => {
  return dictionary[query.trim()] ?? inputLines[Number(query)];
}).join('\n');

console.log(ans);
