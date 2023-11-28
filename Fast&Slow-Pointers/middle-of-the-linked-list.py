# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        #fast = head
        while(fast != None and fast.next !=None):
            slow = slow.next
            fast = fast.next.next
        #print(slow.val)
        return slow