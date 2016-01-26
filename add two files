
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = l1
        carry = (l1.val+l2.val) / 10
        l1.val = (l1.val+l2.val) % 10
        while l1.next != None and l2.next !=None:
            carry += l1.next.val
            carry += l2.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
            l2 = l2.next
        if l1.next == None:
            l1.next = l2.next
        while l1.next != None:
            carry += l1.next.val
            l1.next.val = carry % 10
            carry = carry // 10
            l1 = l1.next
        if carry > 0:
            l1.next = ListNode(carry)
        return head
