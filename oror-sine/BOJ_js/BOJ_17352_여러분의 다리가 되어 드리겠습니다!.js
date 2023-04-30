// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

/**
 * x 가 속한 트리의 루트 노드를 반환한다.
 * @param {Number[]} rep 부모 노드 배열
 * @param {Number} x 자식 노드
 * @returns {Number} 루트 노드
 */
const findSet = function findSet(rep, x) {
  while (x !== rep[x]) x = rep[x];
  return x;
}

/**
 * a, b 가 속한 트리를 합한 뒤 갱신된 부모 노드 배열을 반환한다.
 * @param {Number[]} rep 부모 노드 배열
 * @param {Number} a 자식 노드
 * @param {Number} b 자식 노드
 * @returns {Number[]} `rep` 부모 노드 배열
 */
const unionSet = function unionSet(rep, a, b) {
  const [A, B] = [findSet(rep, a), findSet(rep, b)];
  A < B ? rep[A] = B : rep[B] = A;
  return rep
}

// const rep = String(readFileSync('input.txt')).trim().split('\n')
const rep = String(readFileSync('/dev/stdin')).trim().split('\n')
  .reduce((acc, line) => (
    acc === null
      ? Array.from({ length: Number(line) + 1 }, (_, i) => i)
      : unionSet(acc, ...line.trim().split(' ').map(Number))
  ), null);

const acc = findSet(rep, 1); let x = 2;
while (acc === findSet(rep, x)) x++;
console.log(acc, x);
