// not solved

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var str = x.toString();
    if (str === '0' || x > Math.pow(2, 31) - 1 || x < -Math.pow(2, 31)) return 0;
    else if (str[0] !== '-') return parseInt(str.split('').reverse().join('').replace(/^0+/, ''));
    else return parseInt('-' + str.substr(1, str.length).split('').reverse().join('').replace(/^0+/, ''));
};

console.log(reverse(123));
console.log(reverse(-123));
console.log(reverse(120));
console.log(reverse(0));
console.log(reverse(901000));
console.log(reverse(-2147483648));
-2147483412
-2147483648