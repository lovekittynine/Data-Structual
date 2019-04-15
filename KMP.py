'''
KMP:实现子串的查找
'''

def get_next(T):
    '''
    通过递归得到子串T的next数组
    由第i个位置得到第i+1个位置的next值
    '''
    # 初始化next[0]=-1
    next=[-1]
    # 初始化前缀i,后缀j
    i=0;j=-1
    while (i<len(T)-1):
        if j==-1 or T[i]==T[j]:
            i += 1
            j += 1
            # j也代表<0--i-1>子串中最大前后缀相同的长度为j
            # next[i]=j
            next.append(j)
        else:
            # 将j回溯到次大的前后缀
            j = next[j]
    return next

def get_nextval(T):
    '''
    通过递归得到子串T的nextval数组
    由第i个位置得到第i+1个位置的next值
    '''
    # 初始化next[0]=-1
    next=[-1]
    # 初始化前缀i,后缀j
    i=0;j=-1
    while (i<len(T)-1):
        if j==-1 or T[i]==T[j]:
            i += 1
            j += 1
            # j也代表<0--i-1>子串中最大前后缀相同的长度为j
            # next[i]=j
            if T[i]!=T[j]:
                next.append(j)
            else:
                next.append(next[j])
        else:
            # 将j回溯到次大的前后缀
            j = next[j]
    return next


def KMP(S,T):
    '''
    使用KMP算法从主串S中找到子串T的索引，若没找到返回-1
    '''
    # 得到T的next数组
    next = get_nextval(T)
    # S和T的起始位置
    i=0;j=0
    while (i<len(S) and j<len(T)):
        # 若当前字符匹配成功，则继续比较下一个
        if S[i]==T[j] or j==-1:
            # print('matching %d,%d'%(i,j))
            i += 1
            j += 1
        else:
            # 若匹配失败,则调到下一个j
            j = next[j]
            # print(j)
    if j==len(T):
        # 若匹配成功则返回索引
        return i-j
    else:
        return -1


if __name__ == '__main__':
    T = 'abcdaabcdefadcdeaab'
    S = 'asdasbdasdabcdaabcdefadcdeaabasdasdf'
    next1 = get_next(T)
    next2 = get_nextval(T)
    print(next1,next2)
    index1 = KMP(S,T)
    index2 = S.index(T)
    print(index1,index2)
