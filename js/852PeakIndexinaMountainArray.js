/**
 * @param {number[]} A
 * @return {number}
 */
let peakIndexInMountainArray1 = A => {
    let peak = -1, index = -1;
    A.forEach((v, i) => {
        if (v > peak) {
            peak = v;
            index = i;
        }
    });
    return index;
};

// my second solution
let peakIndexInMountainArray2 = A => A.indexOf(Math.max(...A));

/////////////////////////////////
// best practice 1 : Linear Scan
let peakIndexInMountainArray3 = A => {
    let i = 0;
    while(A[i] < A[i + 1]) i++;
    return i;
}

// best practice 2 : Binary Search
let peakIndexInMountainArray4 = A => {
    let lo = 0, hi = A.length - 1
    while (lo < hi) {
        let mi = (lo + hi) / 2
        if (A[mi] < A[mi + 1]) lo = mi + 1
        else hi = mi
    }
    return lo
}

console.log(peakIndexInMountainArray([0,1,0])); // 1
console.log(peakIndexInMountainArray([0,2,1,0])); // 1