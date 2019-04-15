'''
求所有字符串的最长前缀
'''
inputs = ['flower','flow','flasdbc']
outputs = []

def MaxPre(strs):
    length = [len(string) for string in strs]
    min_len = min(length)
    flag = False
    for i in range(min_len):
        current_char = inputs[0][i]
        for string in strs[1:]:
            if current_char!=string[i]:
                flag = True
                break
        if not flag:
            outputs.append(current_char)
        else:
            break
    if len(outputs)>0:
        print(''.join(outputs))
    else:
        print('')
        
