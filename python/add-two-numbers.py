# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            dig1 = l1.val if l1 != None else 0
            dig2 = l2.val if l2 != None else 0

            sum = dig1 + dig2 + carry
            carry = sum // 10
            dig3 = sum % 10

            tail.next = ListNode(dig3)
            tail = tail.next

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        ans = head.next
        head = None
        return ans
        