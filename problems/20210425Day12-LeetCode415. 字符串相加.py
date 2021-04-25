
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和


def addStrings(num1, num2):
    i = len(num1) - 1  # 从num1的尾部开始计算
    j = len(num2) - 1  # 从num2的尾部开始计算
    add = 0  # add为进位
    ans = ''  # ans为结果
    while(i>=0 or j>= 0 or add != 0):  # i位上还有数 或 j位上还有数 或 有进位
        if i < 0:  # i位没有数的话，i取0
            i = 0
        else:
            x = ord(num1[i]) - ord('0')  # 计算ASCII码
        if j < 0:
            j = 0
        else:
            y = ord(num2[j]) - ord('0')  #  计算ASCII码
        result = x + y + add  # 计算每位上的结果
        ans += str(result % 10)  # 每位的结果加入ans
        add = result // 10  # 计算进位
        i -= 1
        j -= 1
    return ans[::-1]


num1='11'
num2='123'
print(addStrings(num1,num2))