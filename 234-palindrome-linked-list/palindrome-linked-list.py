# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle element.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow will turn out to be the middle element.
        # reverse the second half of the code.
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # check for palindrome by comparing.
        firstlist = head
        secondlist = prev
        while secondlist:
            if firstlist.val != secondlist.val:
                return False
            firstlist = firstlist.next
            secondlist = secondlist.next
        return True
