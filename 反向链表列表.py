'''
Input: 1->2->3->null
Output: 3->2->1->null
'''
#解法一
class Solution:
    def fun(self,head):
        p,rev = head,None
        while p:
            rev,rev.next,p = p, rev, p.next
        return rev



#解法二
def fun2(self,head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

#解法三递归

class Solution:
    def reverseList(self, head):
        def help(head):
            if head == None or head.next == None:
                return head
            pre,last = head(head.next)
            last.next = head
            head.next = None
            return pre,head
        rt,_ = help(head)
        return rt
