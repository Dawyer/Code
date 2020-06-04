# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#  
#
# 示例 1：
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class MysingleLinkList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add(self, val):
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                fount = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        if not self.search(item):
            return

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def getAllData(self):
        data = []
        current = self.head
        while current:
            data.append(current.getData())
            current = current.getNext()
        return data

linkList=MysingleLinkList()
for i in range(10,50,5):
    linkList.add(i)
print(linkList.size())
print(linkList.getAllData())
linkList.remove(25)
print(linkList.getAllData())
linkList.search(25)
linkList.isEmpty()



# def middleNode(head):
#     A = [head]
#     while A[-1].next:
#         A.append(A[-1].next)
#     return A[len(A) // 2]

input_1 = [1, 2, 3, 4, 5]
input_2 = [1, 2, 3, 4, 5, 6]

