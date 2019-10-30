# coding: utf-8
'''
在这里实现栈的一些应用：括号配对检查、进制转换、中缀表达式转后缀表达式
'''
from my_stack import Stack


def par_checker(text):
    '''
    括号匹配，这里只考虑大、中、小括号。
    算法思路很简单，从左到右遍历文本，左括入栈，遇右括出栈，出栈时检查匹配与否；遍历完检索栈内是否还有元素
    :param text: 输入文本
    :return: True or False
    '''
    result = True
    stack = Stack()
    left_par = '([{'
    right_par = {')': '(', ']': '[', '}': '{'}
    for i in text:
        if i in left_par:
            stack.push(i)
        if i in right_par.keys():
            if stack.is_empty():
                result = False
                break
            pop_item = stack.pop()
            if pop_item != right_par[i]:
                result = False
                break

    if not stack.is_empty():
        result = False

    return result


def decimal_convert(num, convert_to=2):
    '''将十进制数转换成其它进制数，以字符串返回
    算法思路就是用十进制数除以N（进制），取余，直至结果为0。最后的余数为新进制数的最高位，符合栈的后进先出特点，故用栈存储余数。

    :param num: int, 十进制数字
    :param convert_to: int, 要转换的进制
    :return: str， 转换后的数字
    '''
    if not num:
        return '0'

    stack = Stack()
    # 这个技巧非常漂亮。将余数的数字与字母对应起来（十六进制场景）
    ch = '0123456789ABCDEF'
    while num // convert_to:
        item = num % convert_to
        num = num // convert_to
        stack.push(item)

    if num:
        stack.push(num)

    res = ''
    while not stack.is_empty():
        res += str(ch[stack.pop()])

    return res

def express_convert(text):
    '''将中缀表达式转换成后缀表达式
    看懂算法的前提是了解中缀表达式转换后缀表达式的过程；
    明确表达式包含的元素：1）操作数，这里将操作数抽象为a-z，即26个小写字母集合；
                        2）操作符，+-*/，+-同等优先级，*/同等优先级并且优先级高于+-
                        3）小括号。小括号内的表达式要先算
    示例：
    a + b + c   ==>   ab+c+
    a + b * c   ==>   abc*+
    a * (b + c) ==>   abc+*
    a + (b + c) * d == > a b c + d * +
    算法流程：
    0）用result_list存储结果
    1）遇操作数，将其append进result_list
    2）遇操作符，如栈内无元素，入栈；
                如栈内有元素，与栈顶元素比较优先级；比栈顶优先级高，则入栈，小于或等于，则弹出栈顶元素并append到result_list，再入
    3）遇左括号，入栈；
    4）遇右括号，不断弹出栈顶操作符，直至弹出左括号。
    :param text: str, 中缀表达式
    :return: str, 后缀表达式
    '''
    text = text.replace(' ', '')
    result_list = []
    stack = Stack()
    priority = {'(': 1, '*': 2, '/': 2, '+': 3, '-': 3}
    for i in text:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            result_list.append(i)
        elif i in '+-*/(':
            if not stack.is_empty():
                top_item = stack.get_top()
                if top_item != '(' and priority[i] >= priority[top_item]:
                    item = stack.pop()
                    result_list.append(item)
            stack.push(i)
            # print(stack.get_items())
        elif i in ')':
            while True:
                item = stack.pop()
                if item == '(':
                    break
                result_list.append(item)

    while not stack.is_empty():
        item = stack.pop()
        result_list.append(item)

    return ' '.join(result_list)


# text = 'a + (b + c) * d'
# print(express_convert(text))
