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
var addTwoNumbers = function(l1, l2) {
    var dummyHead = new ListNode(0);
    var carry = 0, p = l1, q = l2, cur = dummyHead;
    while (p !== null || q !== null) {
        var pval = p !== null ? p.val : 0;
        var qval = q !== null ? q.val : 0;
        var sum = pval + qval + carry;
        cur.next = new ListNode(sum % 10);
        carry = Math.floor(sum / 10);
        p = p && p.next;
        q = q && q.next;
        cur = cur.next;
    }
    if (carry > 0) cur.next = new ListNode(carry);
    return dummyHead.next;
}

function ListNode(val) {
    this.val = val;
    this.next = null;
}

var a = new ListNode(1);
a.next = new ListNode(8);
var b = new ListNode(0);
console.log(addTwoNumbers(a, b));