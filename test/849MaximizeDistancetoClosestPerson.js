/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    var max = 0;
    var maxi = -1;
    seats = seats.join('').split('1');
    seats.forEach((v, i) => {
        if (v.length > max) {
            max = v.length;
            maxi = i;
        }
    });
    // if (max === seats[seats.length - 1].length) 
    return (maxi === 0 || maxi === seats.length - 1) ? max : Math.ceil(max/2);
};

console.log(maxDistToClosest([1,0,0,0,1,0,1])); // 2
console.log(maxDistToClosest([1,0,0,0])); //3
console.log(maxDistToClosest([0,1,0,0,0,0]));   // 4
console.log(maxDistToClosest([0,1,0,0,0,1,1,0,1,1])); // 2
console.log(maxDistToClosest([0,1,1,1,0,0,1,0,0])); // 2

// 1 -> 1
// 2 -> 1
// 3 -> 2
// 4 -> 2
// 5 -> 3
// 6 -> 3
// 7 -> 4
// 8 -> 4