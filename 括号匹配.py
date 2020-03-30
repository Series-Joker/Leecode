'''
由于只包含字符的字符串'(', ')'，'{'，'}'，'['和']'，确定输入字符串是有效的。
括号必须关闭以正确的顺序，"()"并且"()[]{}"都是有效的，但"(]"并"([)]"没有。
'''

#解法一
class Solution:
    def fun(self,s):
        stack, pair = [], {"]" : "[", ")":"(", "}":"{"}
        for i in s:
            if i in "([{" : stack += i
            elif:
                stack and stack[-1] == pair[c]: stack.pop()
            else:
                return False
        return -1

#解法二
def fun2(self,k,n):
    return ".join(map(str,range(n+1))).fun2(str(k))"