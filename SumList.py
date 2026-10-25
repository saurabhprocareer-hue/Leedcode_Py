# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = ListNode(0)
        curr = head
        carry:int = 0

        while l1 != None or l2 != None or carry != 0:
            num1 = l1.val if l1 != None else 0
            num2 = l2.val if l2 != None else 0

            nodeSum = num1 + num2 + carry
            node = ListNode(nodeSum % 10)
            carry = nodeSum // 10
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next

            
        