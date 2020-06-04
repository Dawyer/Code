# 最长回文子串
# 动态规划
class Solution(object):
    def longestPalindrome(self,s):
        '''
        :param s: str
        :return: str
        '''
        maxlen=0
        answer=''
        matrix=[[0 for k in range(len(s))] for k in range(len(s))]
        for j in range(len(s)):
            #i从0到j
            for i in range(0,j+1):
                # matrix对角线为1，有两个相邻并相同
                if j-i<=1:
                    if s[i]==s[j]:
                        matrix[i][j]=1
                        if j-i+1>maxlen:
                            maxlen=j-i+1
                            answer=s[i:j+1]
                if j-i>1:
                    if s[i]==s[j] and matrix[i+1][j-1]:
                        matrix[i][j]=1
                        if j-i+1>maxlen:
                            maxlen=j-i+1
                            answer=s[i:j+1]
        print(matrix)
        return answer

if __name__ == "__main__":
    s="babad"
    sl=Solution()
    print(sl.longestPalindrome(s))
