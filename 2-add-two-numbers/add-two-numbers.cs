/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        var ans = new ListNode();
        var cur = ans;
        var carry = false;

        while (l1 != null || l2 != null){
            if (l1 != null){
                cur.val+=l1.val;
            }
            if (l2 != null){
                cur.val +=l2.val;
            }
            if (carry ) {
                cur.val+=1;
                carry = false;
                }
            if (cur.val >=10) carry = true;
            cur.val %=10;
            if (l1 != null)  l1 = l1.next;
            if(l2!=null ) l2 = l2.next;
            if( l1!= null || l2!=null){
            var temp = new ListNode();
            cur.next = temp;
            cur = cur.next;}
        }
        if (carry){
            cur.next = new ListNode();
            cur.next.val = 1;
        }
        return ans;
    }
}