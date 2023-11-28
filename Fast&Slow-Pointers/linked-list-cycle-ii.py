# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/problems/linked-list-cycle-ii/description/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return None
        slow = fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                slow2=head
                while(slow2 !=slow):
                    slow = slow.next
                    slow2 = slow2.next
                return slow2
        return None