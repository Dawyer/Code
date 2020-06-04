# 最长回文子串
class Solution(object):
    def longestPalindrome(self,s):
        '''
        :param s: str
        :return: str
        '''
        maxlen = 0
        answer = ''
        #i遍历字符串s
        for i in range(len(s)):
            #j遍历i之后的字符串
            for j in range(i,len(s)):
                #取出i和j之间的字符串
                temp = s[i:j+1]
                #temp字符串与翻转后相等即为回文子串
                if temp == temp[::-1] and len(temp)>maxlen:
                    maxlen = len(temp)
                    answer = temp
        return answer

if __name__ == "__main__":
    s="babad"
    sl=Solution()
    print(sl.longestPalindrome(s))
