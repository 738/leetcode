/**
 * @param {number[]} A
 * @return {number}
 */
var peakIndexInMountainArray = function(A) {
    var peak = -1;
    var answer = -1;
    A.forEach((v, i) => {
        if (v > peak) {
            peak = v;
            answer = i;
        }
    });
    return answer;
};

console.log(peakIndexInMountainArray([0,1,0])); // 1
console.log(peakIndexInMountainArray([0,2,1,0])); // 1