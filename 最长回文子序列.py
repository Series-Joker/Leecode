#   回文串：从左边往右读和从右边往左读是一样的
#     数组；s = 'abccccdd'
#      输出：7     dccaccd


'''
解法1：直接遍历数组统计每个字母出现的次数，根据奇数偶数
1，若字母出现的次数为2K次，则答案增加2K
2，若字母出现次数为2k+1,则答案增加2k
3，若存在字母出现为奇数，答案加一

'''
s = 'aasaddafdf'
def fun(self,s):
    hash1 = [0 for i in range(256)]  #记录字符出现的次数
    for i in s:
        hash1[ord[i]] += 1

    ans = 0
    odd = 0    # 有基数词的字符
    for (char,num) in hash1.items():
        if num & 2 == 0:
            ans += num
        else:
            ans += num - 1
            odd = 1
    ans += odd  #加上一个出现基数词的字符
    return ans
fun(s)


'''
解法2：用set保存出现了奇次数的字符
1，遍历数组
2，若一个字符在set中，将其从set删除
3，若不在，将其加入set
答案 = len(s) - len(set) - 1) (if len(set) >0)

'''
def fun2(self,s):
    hash2 = {}
    for j in s:
        if j in hash2:
            del hash2[j]
        else:
            hash2[j] = True

    remove = len(hash2)
    if len(hash2) == 0:
        return len(s)
    else:
        return len(s) - len(hash2) + 1
