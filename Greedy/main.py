from itertools import permutations

def oper(a, b, char):
    if char == '-':
        return a - b
    elif char == '+':
        return a + b
    elif char == '*':
        return a * b
    else:
        return

def solution(expression):
    tmp = ''
    op_list = []
    num_list = []
    permu = ['*','-','+']
    for char in expression:
        if char == '-':
            num_list.append(tmp)
            op_list.append('-')
            tmp = ''
        elif char == '+':
            num_list.append(tmp)
            op_list.append('+')
            tmp = ''
        elif char == '*':
            num_list.append(tmp)
            op_list.append('*')
            tmp = ''
        else:
            tmp += char
    num_list.append(tmp)
    per_list = list(permutations(permu, 3))
    max = 0
    for per in per_list:
        op_list_copy = op_list.copy()
        num_list_copy = num_list.copy()
        for op in per:
            while True:
                if op in op_list_copy:
                    index = op_list_copy.index(op)
                else:
                    break
                sub_sum = oper(int(num_list_copy[index]), int(num_list_copy[index + 1]), op)
                op_list_copy.pop(index)
                num_list_copy.pop(index)
                num_list_copy.pop(index)
                num_list_copy.insert(index, sub_sum)
        if max < abs(num_list_copy[0]):
            max = abs(num_list_copy[0])
    return max