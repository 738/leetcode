/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    var i = 0, j = 0;
    var num1 = 0, num2 = 0;
    while (l1.next !== null) {
        // var num1 += l1.val * Math.pow(10, i++);
    }

    while (l2.next !== null) {
        // var num2 += (l2.val * Math.pow(10, j++));
    }

    return num1 + num2;
};


function ListNode(val) {
    this.val = val;
    this.next = null;
}