"""
实现快速排序算法
"""

def getPartition(array,low,high):
    """
    双指针法，每次找到中枢(pivot)所在下标
    """
    # pivot值
    pivotKey = array[low]
    while low<high:
        # 需要注意至少需要一个等号，否者当遇到2个元素相等时会陷入死循环
        while low<high and array[high]>=pivotKey:
            # pivot右边的值应该都比pivot大
            high -= 1
        # 否者将右边比pivot小的值和pivot交换位置
        # 将其移动到pivot左边
        array[low],array[high] = array[high],array[low]
        while low<high and array[low]<pivotKey:
            # pivot左边的值应该都比pivot小
            low += 1
        # 否者将比pivot大的值移动到右边
        array[low],array[high] = array[high],array[low]
    return low


def quick_sort(array,low,high):
    # 退出递归条件
    if low<high:
        partition = getPartition(array,low,high)
        # 对左半部分划分
        quick_sort(array,low,partition-1)
        # 对右半部分划分
        quick_sort(array,partition+1,high)



if __name__ == '__main__':
    import numpy as np
    np.random.seed(1)
    li = np.random.randint(1,100,10).tolist()
    print('排序前:',li)
    # print(getPartition(li,0,len(li)-1))
    quick_sort(li,0,len(li)-1)
    print('排序后:',li)