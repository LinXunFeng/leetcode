"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from ListNode import ListHander, ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 递规
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        # 非递规
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        return head.next
        

if __name__ == "__main__":
    p = [1,2,4]
    q = [1,3,4]
    pList = ListHander.buildSingleDirectionList(p)
    qList = ListHander.buildSingleDirectionList(q)
    res = Solution().mergeTwoLists(pList, qList)
    if res is not None:
        ListHander.printSingleDirectionList(res)
    else:
        print('空')