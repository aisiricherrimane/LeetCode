# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            next = curr.next
            prev.next = next
            curr.next = next.next
            next.next = curr

            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr

        return dummy.next
            

        