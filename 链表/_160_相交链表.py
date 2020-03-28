"""
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

在节点 c1 开始相交。

示例：
A:          4 → 1
                   ↘
                     8 → 4 → 5
                   ↗            
B:      5 → 0 → 1

相交节点的值为 8

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from ListNode import ListHander, ListNode

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headALen = self.getListLength(headA)
        headBLen = self.getListLength(headB)
        curA = headA
        curB = headB
        diff = headALen - headBLen
        delta = abs(diff)
        if diff > 0: # A长
            lowLen = headBLen
            while delta:
                curA = curA.next
                delta -= 1
        else: # B长 或 长度相等
            lowLen = headALen
            while delta:
                curB = curB.next
                delta -= 1
        while lowLen:
            # if curA.val == curB.val: # 题目中是节点相同才是同一个节点，值相同不一定的同一个节点
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
            lowLen -= 1
        return None

    def getListLength(self, head):
        if head is None:
            return 0
        curHead = head
        length = 1
        while curHead.next:
            curHead = curHead.next
            length += 1
        return length


if __name__ == "__main__":
    p = [4,1,8,4,5]
    q = [5,0,1,8,4,5]
    pList = ListHander.buildSingleDirectionList(p)
    qList = ListHander.buildSingleDirectionList(q)
    res = Solution().getIntersectionNode(pList, qList)
    print(res)
