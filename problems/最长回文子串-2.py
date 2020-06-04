# 最长回文子串
class Solution(object):
    def longestPalindrome(self,s):
        '''
        :param s: str
        :return: str
        '''
        maxlen=''
        for i in range(len(s)):
            #类似aba
            temp = self.helper(s,i,i)
            if len(temp)>len(maxlen):
                maxlen=temp
            #类似abba
            temp = self.helper(s,i,i+1)
            if len(temp)>len(maxlen):
                maxlen=temp
        return maxlen

    def helper(self,s,l,r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

if __name__ == "__main__":
    s="babbad"
    sl=Solution()
    print(sl.longestPalindrome(s))
