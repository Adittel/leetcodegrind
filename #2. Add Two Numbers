#2. Add Two Numbers
# thiis is a program to add 2 linked lists.
# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x= ListNode(None)
        dummy=x
        carry =False
        while(l1!=None and l2!=None):
            
            holder=l1.val+l2.val
            if(carry):
                holder+=1
                carry=False
            if(holder>=10):
                holder-=10
                carry=True
            x.val=holder
            x.next= ListNode(None)
            x=x.next
            l1=l1.next
            l2=l2.next
        #remove last node
        if(l1):
            
            while(l1!=None):   
                 
                holder=l1.val
                if(carry):
                    holder+=1
                    carry=False
                if(holder>=10):
                    holder-=10
                    carry=True
                x.val=holder
                x.next= ListNode(None)
                x=x.next
                l1=l1.next
        if(l2):
            
            while(l2!=None):
                holder=l2.val
                if(carry):
                    holder+=1
                    carry=False
                if(holder>=10):
                    holder-=10
                    carry=True
                x.val=holder
                x.next= ListNode(None)
                x=x.next
                l2=l2.next
        if(carry):
            x.val=1
            return dummy
        dummy2=dummy
        while(dummy2.next.next):
            dummy2=dummy2.next
            print("k")
        dummy2.next=None
        return dummy     

