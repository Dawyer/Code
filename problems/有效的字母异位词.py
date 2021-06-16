'''
第53天
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
'''
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 思路：
        # dict_s,dict_t两个字典
        # 键为s,t的字符，值为字符出现的次数，最后判断字典是否相等
        # 可以使用collections.Counter方法
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in s:
            dict_s[i] = s.count(i)
        for j in t:
            dict_t[j] = t.count(j)
        print(dict_s)
        print(dict_t)
        print(collections.Counter(s))
        print(collections.Counter(t))
        return dict_s == dict_t


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("aacc", "ccac"))