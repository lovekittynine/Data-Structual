"""
增量(incremental)不断缩小的插入排序
将一个序列分成多个子序列，对每个子序列进行插入排序
按照incremental每次取得一个子序列
"""

def shell_sort(array):
    nums = len(array)
    # 初始化增量
    incremental = nums//2
    while incremental>=1:
        # 插入排序从第二个元素开始，默认第一个元素有序
        # 每个子序列的第二个元素从incremental开始
        for i in range(incremental,nums):
            # 步长为incremental
            for j in range(i,0,-incremental):
                # 下一个元素是j-incremental
                if array[j]<array[j-incremental]:
                    array[j],array[j-incremental] = array[j-incremental],array[j]
                else:
                    break
        # 对所有子序列执行完一次插入排序后
        # 增量折半
        incremental = incremental // 2
    return array


if __name__ == '__main__':
    li = [23,12,23,55,28,46,90,100,77]
    print("排序前:",li)
    li = shell_sort(li)
    print("排序后:",li)