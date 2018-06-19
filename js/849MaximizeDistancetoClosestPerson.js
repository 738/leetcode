/**
 * @param {number[]} seats
 * @return {number}
 */
let maxDistToClosest = seats => {
    let max = 0;
    seats.join('').split('1').forEach((v, i, a) => {
        let tmp = (i === 0 || i === a.length - 1) ? v.length : Math.ceil(v.length/2);
        if (tmp > max) max = tmp;
    });
    return max;
};

console.log(maxDistToClosest([1,0,0,0,1,0,1])); // 2
console.log(maxDistToClosest([1,0,0,0])); //3
console.log(maxDistToClosest([0,1,0,0,0,0]));   // 4
console.log(maxDistToClosest([0,1,0,0,0,1,1,0,1,1])); // 2
console.log(maxDistToClosest([0,1,1,1,0,0,1,0,0])); // 2
console.log(maxDistToClosest([0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0])) // 3
console.log(maxDistToClosest([0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1])) // 3

// 1 -> 1
// 2 -> 1
// 3 -> 2
// 4 -> 2
// 5 -> 3
// 6 -> 3
// 7 -> 4
// 8 -> 4

// 1 -> 1
// 2 -> 2
// 3 -> 3
// 4 -> 4
// 5 -> 5