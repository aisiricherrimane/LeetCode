# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val= 0, next=None):
#       self.val = 0
#        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else 0
                temp.append(self.mtwo(l1, l2))
            lists = temp
        return lists[0]

    def mtwo(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1

        if l2:
            temp.next = l2

        return dummy.next   