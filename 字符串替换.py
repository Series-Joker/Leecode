'''
给定两个相同大小的字符串A和B,再给一个字符串S,所有出现在S里的子串A[i]
都要替换成B[i].

A = ['ab','aba','cba']
B = ['cc','ccc','abd']
s = 'ababa'
Ans = 'cccba'
'''
'''
1，计算所有模式串的哈希值
2，计算需要替换字符串的s[0:i]的哈希值
3，遍历所有的模式串。看是否能替换
4，对于可替换的部分进行替换
5，对于字符串S的每个位置进行操作3和4
'''
def fun(a,b,s):
    send = 31
    mod = 10**9+7

    targetHash = []  #A的哈希值
    sourceHash = []   # = s[0,i]的哈希值
    base = []  #bash[i] = 31** I

    #求模式串的哈希值
    for i in a:
        temp = 0
        for j in i:
            temp = (temp * send + ord(j) - ord('a')) % mod
        targetHash.append(temp)

    temp = 0
    sourceHash.append(temp)



