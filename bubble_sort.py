
# bubble sort1
# 直接选择每一轮的最小值
import numpy as np
np.random.seed(0)

def bubble_sort(array):
    '''
    每一次选择一个最小的值
    '''
    import time
    start = time.time()
    nums = len(array)
    for i in range(nums-1):
        for j in range(i+1,nums):
            if array[j]<array[i]:
                array[i],array[j] = array[j],array[i]
    end = time.time()
    print("Time Elapsed:",end-start)
    return array


def bubble_sort2(array):
    """
    每一次得到最小元素的索引
    最后在交换，减少交换次数
    """
    import time
    start = time.time()
    nums = len(array)
    for i in range(nums-1):
        min_ind = i
        for j in range(i+1,nums):
            if array[j]<array[min_ind]:
                min_ind = j
        # 交换一次
        array[i],array[min_ind] = array[min_ind],array[i]
    end = time.time()
    print("Time Elapsed:",end-start)
    return array


def bubble_sort3(array):
    """
    标准冒泡排序，两两比较
    """
    import time
    start = time.time()
    nums = len(array)
    # 外层循环n-1次
    for i in range(0,nums-1):
        # 内层循环两两比较
        # nums-i-1(-1)为了满足j+1不超过索引下标
        count = 0
        for j in range(0,nums-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                count += 1
        # 冒泡排序的改进，引入count
        # 如果count=0,说明数组已经有序
        # 直接退出
        if count == 0 :
            break
    end = time.time()
    print("Time Elapsed:",end-start)
    return array



if __name__ == '__main__':
    li = np.random.randint(0,1000,10000).tolist()
    # li = sorted(li)
    # print("排序前:",li)
    li = bubble_sort3(li)
    # print("排序后:",li)