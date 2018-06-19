/**
 * @param {number[]} A
 * @return {number}
 */
// let peakIndexInMountainArray = A => {
//     let peak = -1, answer = -1;
//     A.forEach((v, i) => {
//         if (v > peak) {
//             peak = v;
//             answer = i;
//         }
//     });
//     return answer;
// };

let peakIndexInMountainArray = A => A.indexOf(Math.max(...A));

console.log(peakIndexInMountainArray([0,1,0])); // 1
console.log(peakIndexInMountainArray([0,2,1,0])); // 1