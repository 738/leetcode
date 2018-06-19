/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var ss = s.split(' ');
    for (let i = ss.length - 1; i >= 0; i--) {
        if (ss[i].length !== 0) return ss[i].length;
    }
    return 0;
};