# 今天三月三，努力刷题，努力找工作
#
#
#
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
# 示例：
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
# 提示：
# 1 <= word.length, prefix.length <= 2000
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次


# 开始用列表解决，第14个例子没过，看题解发现根本不是一回事，学习到了
# 参考负雪明烛
# 前缀树（只保存小写字符的）「前缀树」是一种特殊的多叉树，
# 它的 TrieNode 中 chidren 是一个大小为 26 的一维数组，
# 分别对应了26个英文字符 'a' ~ 'z'，也就是说形成了一棵 26叉树。
# 前缀树的结构可以定义为下面这样。
# 里面存储了两个信息：
# isWord 表示从根节点到当前节点为止，该路径是否形成了一个有效的字符串。
# children 是该节点的所有子节点。
#
# 跟二叉树类似先建一个树
# get取字典的值
# defaultdict初始化给key默认值,使用的是字典，保存的结构是{字符:Node}
import collections


class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)