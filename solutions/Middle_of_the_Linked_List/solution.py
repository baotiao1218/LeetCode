# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while(fast.next != None):
            slow = slow.next
            
            if(fast.next.next != None):
                fast = fast.next.next
            else:
                fast = fast.next

        return slow

## Time Complexity:O(n)
## Space complexity:O(1)


#Optimized Answer
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        #精簡while條件, 且fast走超過沒差, slow一樣會在中位數
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow 
    
## Time Complexity:O(n)
## Space complexity:O(1)