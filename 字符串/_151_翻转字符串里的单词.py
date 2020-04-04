"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        arr = list(s)
        # 消除多余的空格
        length = 0 # 最终字符串的有效长度
        cur = 0 # 当前可替换字符的位置
        isSpace = True # 前一位是否为空字符(初始化值为True，可忽略开头的空字符串)
        for i in range(len(arr)):
            if arr[i] != " ":
                arr[cur] = arr[i]
                cur += 1
                isSpace = False
            else:
                if isSpace:
                    continue
                arr[cur] = arr[i]
                cur += 1
                isSpace = True
        length = cur-1 if isSpace else cur
        if length <= 0: # 原字符串全是空字符
            return ""

        # 整体逆序
        self.reverse(arr, 0, length)

        # 每个单词逆序
        preSpaceIndex = -1 # 前一个空字符的下标
        for i in range(length):
            if arr[i] != " ":
                continue
            self.reverse(arr, preSpaceIndex+1, i)
            preSpaceIndex = i
        # 逆序最后一个单词
        self.reverse(arr, preSpaceIndex+1, length)
        
        return "".join(arr[:length])

    def reverse(self, arr, left, right):
        """
        将[left, right)范围内的元素进行逆序
        """
        right -= 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    str = "the sky is blue"
    str = "  hello  world"
    str = ""
    res = Solution().reverseWords(str)
    print(res)