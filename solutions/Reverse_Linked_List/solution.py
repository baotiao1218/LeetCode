#My Original Answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = r = head

        if(head == None):
            return None
        if(p.next == None):
            return head
        if(p.next.next == None):
            q = p.next
            p.next = None
            q.next = p
            return q
        
        q = p.next
        r = q.next
        p.next = None

        while(r != None):
            q.next = p
            p = q
            q = r
            if(r.next == None):
                q.next = p
                return q
            else:
                r = r.next

####: init p q r, p = head, q = 1, r = 2

## Time Complexity:O(1)
## Space complexity:O(1)

#Optimized Answer 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node

####: init p q r, p = -1, q = head

## Time Complexity:O(1)
## Space complexity:O(1)