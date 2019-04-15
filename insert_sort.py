# 直接插入排序
# 从右边往左找到合适的插入位置

def insert_sort(array):
    nums = len(array)
    # 假设第一个位置有序，从第二个位置开始
    for i in range(1,nums):
        # 让前i个元素有序
        for j in range(i,0,-1):
            # 如果第j个元素大于第j-1个元素
            # 则交换，否则已经有序则退出内循环
            if array[j]<array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break
    return array

def insert_sort2(array):
    nums = len(array)
    # 假设第一个位置有序，从第二个位置开始
    for i in range(1,nums):
        # 让前i个元素有序
        j = i
        while j>0:
            if array[j]<array[j-1]:
                array[j-1],array[j] = array[j],array[j-1]
                j -= 1
            else:
                break
    return array



if __name__ == '__main__':
    import numpy as np
    np.random.seed(0)
    li = np.random.randint(0,1000000,10).tolist()
    print("排序前:",li)
    li = insert_sort2(li)
    print("排序后:",li)
