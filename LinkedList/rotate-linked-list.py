# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next==None or k==0:
            return head
        count = 1
        last = head
        while(last.next != None):
            last = last.next
            count+=1
        k = k%count
        last.next = head

        temp = head
        for _ in range(count -k -1):
            temp = temp.next
        res = temp.next
        temp.next = None
        return res
        
                      