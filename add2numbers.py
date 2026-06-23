class Solution:
    def addTwoNumbers(self, l1: listnode, l2: listnode) -> listnode:
        dummy=listnode(0)
        carry=0
        temp=dummy
        while l1 or l2 or carry!=0:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            num = val1+val2+carry
            val = num % 10
            carry = num//10
            temp.next=listNode(val)
            temp=temp.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next