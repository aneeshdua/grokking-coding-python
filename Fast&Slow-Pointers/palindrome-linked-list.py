# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def reverseLL(self,head:[ListNode]) -> ([ListNode]):
        main = head
        previous = None
        while(main != None):
            nextPt = main.next
            main.next = previous
            previous = main
            main = nextPt
        return previous

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = fast = head
        while(fast != None and fast.next != None):
            mid = mid.next
            fast = fast.next.next
        
        mid = self.reverseLL(mid)

        start = head
        while(mid != None and start != None):
            if (mid.val != start.val):
                return False
            mid = mid.next
            start = start.next
        return True
        
        