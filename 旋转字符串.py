'''
给出一个字符串，一个右偏移量和一个左偏移量，
根据给出的偏移量循环移动字符串

输入： str='abcd',left = 3,right = 1
输出： ‘cdab

'''
def fun1(self,s,left,right):
    offset = left - right

    offset %= len(s)
    result = s[offset: ] + s[ :offset]
    return result

    