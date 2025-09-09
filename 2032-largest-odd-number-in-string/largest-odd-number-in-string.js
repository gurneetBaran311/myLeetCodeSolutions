/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function (s) {
  let n = s.length - 1;
  while (n > -1) {
    if (Number(s[n]) % 2 == 1) {
      return s.substring(0, n + 1);
    }
    --n;
  }
  return "";
};
