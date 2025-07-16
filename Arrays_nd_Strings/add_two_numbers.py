# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)
        current = result
        carry = 0
        ptr1 = l1
        ptr2 = l2
        while ptr1 or ptr2 :
            value1 = ptr1.val if ptr1 else 0
            value2 = ptr2.val if ptr2 else 0
            sum = value1 + value2 + carry
            digit = sum % 10
            carry = sum // 10
            current.next = ListNode(digit)
            current = current.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
            if carry:
                current.next = ListNode(carry)
        return result.next


        