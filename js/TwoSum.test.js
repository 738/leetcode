// var assert = require('chai').assert;
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    for (var i = 0; i < nums.length; i++)
        for (var j = i + 1; j < nums.length; j++)
            if (nums[i] + nums[j] === target) return [i, j];
};

// // test cases
// describe('TwoSum', function () {
//     let testCases =
//     [
//         [twoSum([2, 7, 11, 15], 9), [0, 1]],
//         [twoSum([1, 7, 2, 15], 9), [1, 2]],
//         [twoSum([2, 7, 11, 15], 18), [1, 2]],
//     ];
//     for (var i = 0; i < testCases.length; i++) {
//         console.log(testCases[i])
//         it(`${testCases[i]}`, function () {
//             assert.deepEqual(testCases[i][0], testCases[i][1]);
//         });
//     }
// })
