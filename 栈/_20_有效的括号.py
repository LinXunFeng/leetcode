"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 栈的解决方法
        # leftFlagList = ["{", "(", "["]
        # rightFlagList = ["}", ")", "]"]
        # leftStack = []
        # rightStack = []
        # for i in s:
        #     leftStack.append(i)
        # while len(leftStack) != 0:
        #     flag = leftStack.pop()
        #     if flag in rightFlagList: # 右括号
        #         rightStack.append(flag)
        #     if flag in leftFlagList: # 左括号
        #         if len(rightStack) == 0:
        #             return False
        #         # 比对括号
        #         rightFlag = rightStack.pop()
        #         if flag == '{' and rightFlag != '}':
        #             return False
        #         if flag == '(' and rightFlag != ')':
        #             return False
        #         if flag == '[' and rightFlag != ']':
        #             return False
        # if len(rightStack) != 0:
        #     return False
        # return True

        # 字符串替换大法
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


if __name__ == "__main__":
    str = "{([{}])}"
    res = Solution().isValid(str)
    print(res)
