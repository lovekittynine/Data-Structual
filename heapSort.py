"""
实现堆排序
堆是一种数据结构：本质上是一个完全二叉树
堆分为大根堆和小根堆
大根堆：双亲结点的数值比孩子结点都大，二叉树的根结点具有最大值
小根堆：双亲结点的数值比孩子结点都小，二叉树的根结点具有最小值
"""


def HeapAdjust(L,s,length):
    """
    将双亲结点为s的子树调整为大根堆
    length:最后一个元素的索引
    """
    temp = L[s]
    while 2*s<length:
        i = 2*s
        if L[i]<L[i+1]:
            i += 1
        if temp>=L[i]:
            break
        L[s] = L[i]
        s = i
    L[s] = temp


def heapSort(L):
    n = len(L)
    # 构建大根堆
    for i in range(n//2-1,-1,-1):
        HeapAdjust(L,i,n)
    # 排序
    # 将根结点与堆数组最后一个元素交换，然后重新调整剩余元素为大根堆
    for i in range(n-1,-1,-1):
        L[0],L[i] = L[i],L[0]
        # 将剩余i-1个元素调整为大根堆
        HeapAdjust(L,0,i-1)


if __name__ == "__main__":
    li = [5,2,1,6,3,4,8,7]
    heapSort(li)
    print(li)
