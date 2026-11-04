# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None :
            return

        fast = head
        slow = head

        for i in range(n):
            if fast is None:
                return None
            fast = fast.next

        if fast is None :
            head = head.next
            return head

        while fast.next :
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head