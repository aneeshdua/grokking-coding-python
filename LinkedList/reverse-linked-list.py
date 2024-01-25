# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        before=None
        curr=head
        while(curr !=None):
            after=curr.next
            curr.next = before
            before = curr
            curr = after
            #after = after.next
            #print(before.val,curr.val,after.val)
        #curr=head
        return before