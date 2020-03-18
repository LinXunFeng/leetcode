# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListHander(object):
    @classmethod
    def buildSingleDirectionList(cls, list):
        """
        构建单向链表
        """
        head = None
        preNode = None
        for i in list:
            node = ListNode(i)
            if head is None:
                head = node
            if preNode is not None:
                preNode.next = node
            preNode = node
        return head

    @classmethod
    def printSingleDirectionList(cls, list):
        """遍历所有节点"""
        print(list.val, end=" ")
        next = list.next
        while next:
            print(next.val, end=" ")
            next = next.next
        print("")


if __name__ == "__main__":
    arr = [1,2,3,4]
    list = ListHander.buildSingleDirectionList(arr)
    ListHander.printSingleDirectionList(list)
