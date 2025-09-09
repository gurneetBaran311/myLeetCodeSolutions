/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let n = height.length;
  let lMax = [],
    rMax = new Array(n).fill(0),
    result = 0;
  ((lMax[0] = height[0]), (rMax[n - 1] = height[n - 1]));
  for (let i = 1; i < n; i++) {
    lMax.push(Math.max(height[i], lMax[i - 1]));
    rMax[n - i - 1] = Math.max(height[n - i - 1], rMax[n - i]);
  }
  for (let i = 0; i < n; i++) {
    let minHeight = Math.min(lMax[i], rMax[i]);
    result += minHeight - height[i];
  }
  return result;
};
