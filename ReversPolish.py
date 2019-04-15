'''
用栈实现逆波兰算法计算四则运算
eg:
'3 5 + 3 *' = (3+5)*3=24
'''
# strip()只能去掉字符串前后二端的空格，中间的无法去除
inputs = '4 13 5 / +'
stack = []

def operate(a,b,operator):

    if operator=="+":
        return a+b
    elif operator=='-':
        return a-b
    elif operator=='*':
        return a*b
    elif operator=='/':
        '''
        除数代表整除
        '''
        return a//b
    else:
        raise Exception('操作符不合法')


def main():
    
    # 用split去除空格
    for char in inputs.split(' '):
        try:
            num = int(char)
            stack.append(num)
        except Exception:
            # 操作数栈
            b = stack.pop()
            a = stack.pop()
            stack.append(operate(a,b,char))
    res = stack.pop()
    print(res)


if __name__ == "__main__":
    main()










