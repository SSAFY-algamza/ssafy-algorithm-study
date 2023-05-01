// import { readFileSync } from "fs";
const fs = require("fs");
const readFileSync = fs.readFileSync;

/** 
 * str 의 start 부터 end 까지가 팰린드롬인지 판별하는 함수
 * @param {(String | String[])} str 문자열 또는 문자의 배열
 * @param {Number} start
 * @param {Number} end
 * @param {Boolean[][]} dp [end][start]
 * @returns {Boolean} `start` 부터 `end` 까지가 팰린드롬인지
 */
const checkPalindrome = function checkPalindrome(str, start, end, dp) {
  if (start === end) return true;
  if (start + 1 === end) return str[start] === str[end];
  if (str[start] === str[end]) return dp[end-1][start+1];
  return false;
};

/**
 * a 와 b 중 작은 숫자를 반환하는 함수
 * @param {Number} a 
 * @param {Number} b 
 * @returns {Number}
 */
const min = function min(a, b) { return a < b ? a : b; };

/** 배열 고차함수 사용을 위해 `String[]`로 바꿔줌 */
// const inputChars = String(readFileSync('input.txt')).trim().split('');
const inputChars = String(readFileSync('/dev/stdin')).trim().split('');


/** @type {Boolean[][]} [end][start]*/
const isPalindrome = inputChars.reduce((dp, _, end, chars) => {
  dp.push(
    chars
      .slice(0, end + 1)
      .map((_, start) => checkPalindrome(chars, start, end, dp))
  );
  return dp;
}, []);

/** @type {Number[]} */
const min_split = isPalindrome.reduce((dp, bools, end) => {
  dp.push(
    bools[0] ? 1 : bools.reduce(
      (prev, bool, start) => bool ? min(prev, dp[start - 1] + 1) : prev, end + 1
    )
  );
  return dp;
}, []);

console.log(min_split.pop());