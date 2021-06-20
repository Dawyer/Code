"""
第55天
一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。
这个王国有一个明确规定的皇位继承顺序，第一继承人总是国王自己。我们定义递归函数Successor(x, curOrder)，
给定一个人x和当前的继承顺序，该函数返回 x的下一继承人。
Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子
比方说，假设王国由国王，他的孩子Alice 和 Bob （Alice 比 Bob年长）和 Alice 的孩子Jack 组成。
一开始，curOrder为["king"].
调用Successor(king, curOrder)，返回 Alice ，所以我们将 Alice 放入 curOrder中，得到["king", "Alice"]。
调用Successor(Alice, curOrder)，返回 Jack ，所以我们将 Jack 放入curOrder中，得到["king", "Alice", "Jack"]。
调用Successor(Jack, curOrder)，返回 Bob ，所以我们将 Bob 放入curOrder中，得到["king", "Alice", "Jack", "Bob"]。
调用Successor(Bob, curOrder)，返回null。最终得到继承顺序为["king", "Alice", "Jack", "Bob"]。
通过以上的函数，我们总是能得到一个唯一的继承顺序。
请你实现ThroneInheritance类：
ThroneInheritance(string kingName) 初始化一个ThroneInheritance类的对象。国王的名字作为构造函数的参数传入。
void birth(string parentName, string childName)表示parentName新拥有了一个名为childName的孩子。
void death(string name)表示名为name的人死亡。一个人的死亡不会影响Successor函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。
string[] getInheritanceOrder()返回 除去死亡人员的当前继承顺序列表。

示例：
输入：
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death",
"getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"],
 ["bob", "asha"], [null], ["bob"], [null]]
输出：
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null,
["king", "andy", "matthew", "alex", "asha", "catherine"]]
解释：
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：king
t.birth("king", "andy"); // 继承顺序：king > andy
t.birth("king", "bob"); // 继承顺序：king > andy > bob
t.birth("king", "catherine"); // 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); // 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]

"""
from collections import defaultdict
from typing import List

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.edges = defaultdict(list)
        self.dead = set()
        self.king = kingName


    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)


    def death(self, name: str) -> None:
        self.dead.add(name)


    def getInheritanceOrder(self) -> List[str]:
        ans = list()
        def preorder(name):
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for childname in self.edges[name]:
                    preorder(childname)
        preorder(self.king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

if __name__ == '__main__':
    s = ThroneInheritance("king")
    s.birth("king", "andy")
    s.birth("king", "bob")
    s.birth("king", "catherine")
    s.birth("andy", "mathew")
    s.birth("bob", "alex")
    s.birth("bob", "asha")
    print(s.getInheritanceOrder())
    s.death("bob")
    print(s.getInheritanceOrder())
