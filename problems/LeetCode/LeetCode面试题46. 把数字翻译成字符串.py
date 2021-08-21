# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
#  
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  
#
# 提示：
#
# 0 <= num < 231


class Solution:
    def translateNum(self, num: int) -> int:
        num=str(num)
        if len(num)==1:
            return 1
        n_minus_2=1
        n_minus_1=1
        res=0
        for i in range(1,len(num)):
            flag=num[i-1:i+1]
            if int(flag)>25 or int(flag)<10:
                res=n_minus_1
            else:
                res=n_minus_1+n_minus_2
            n_minus_2,n_minus_1=n_minus_1,res
        return res

solution = Solution()
print(solution.translateNum(12258))