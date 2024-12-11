/**
 * @param {number} num
 * @return {number[]}
 */
var sumOfThree = function(num) {
  
    if ((num - 3) % 3 === 0) {
        let start = (num - 3) / 3;
        return [start, start + 1, start + 2];
    }
    return [];
};