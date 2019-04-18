"""
二分查找
"""
def binary_search(array,item):
    #初始化头尾指针
    low = 0
    high = len(array)-1
    # 中间位置
    mid = (low+high)//2
    # 注意:二分查找需要注意等号
    # 此时mid = low = high,如果不取等号(则有序数组最左边和最右边的元素查找不到)
    while low<=high:
        if array[mid] == item:
            print(mid)
            return True
        elif array[mid]>item:
            # 在左边查找
            high = mid-1
        else:
            # 在右边查找
            low = mid+1
        # 更新中间值的位置
        mid = (low+high)//2
    # 否者不存在
    print("不存在元素:%d"%item)

if __name__ == "__main__":
    li = [1,2,3,4,5,6,7]
    binary_search(li,7)
    binary_search(li,9)


