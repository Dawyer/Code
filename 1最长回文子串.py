# 最长回文子串
class Solution(object):
    def longestPalindrome(self,s):
        maxlen = 0
        answer = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp)>maxlen:
                    maxlen = len(temp)
                    answer = temp
        return answer

if __name__ == "__main__":
    s="babad"
    sl=Solution()
    print(sl.longestPalindrome(s))
