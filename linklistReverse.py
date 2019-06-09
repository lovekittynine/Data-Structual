"""
链表反转
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList():

    def __init__(self):
        self.head = None

    def append(self,item):
        """
        尾插法
        """
        node = Node(item)
        # 细节：头结点为空的时候要特殊处理
        # 一开始就cur = self.head
        # 当self.head=None时，修改cur指向并不会修改self.head的指向
        # 猜测，self.head=None时，None并没有开辟内存空间
        if self.head is None:
            self.head = node
        else:
            # 当head不为空时，改变cur会改变head的内容
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end=' ')
            cur = cur.next
        print('')


def linklist_Reverse(L):
    """
    链表反转：头插法创建一个新的列表
    """
    cur1 = L.head
    new_link = LinkList()
    while cur1 is not None:
        node = Node(cur1.data)
        # 头插
        node.next = new_link.head
        new_link.head = node
        cur1 = cur1.next
    new_link.traverse()

      
if __name__ == "__main__":
    li = list(range(9))
    linklist = LinkList()
    for a in li:
        linklist.append(a)
    linklist.traverse()
    # print(linklist.head.data)
    linklist_Reverse(linklist)