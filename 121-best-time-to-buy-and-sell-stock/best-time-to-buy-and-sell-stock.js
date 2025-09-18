/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let min = prices[0], diff = 0;
    for (let i in prices) {
        min = Math.min(min, prices[i]);
        diff = Math.max(diff, (prices[i] - min));
    }
    return diff
};