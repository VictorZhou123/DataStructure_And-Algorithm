# class Stack:
#     def __init__(self) -> None:
#         self.stack = []
#     def push(self,element):
#         self.stack.append(element)
#     def pop(self):
#         return self.stack.pop()
#     def get_top(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None



def brace_match(s):
    dic = {"(":")","[":"]","{":"}"}   # 建立字典，方便查询
    tmp = []                          # 存放括号
    for i in s:                       # 遍历字符
        if i in dic:
            tmp.append(i)             # 如果i是左括号中的一种，就压栈
        elif len(tmp) == 0:
            return False              # 如果右括号进行检查时，栈里没有数据则返回false
        elif i == dic.get(tmp.pop()): # 将i与弹出的括号进行匹配，成功则继续循环，失败则返回false
            continue
        else:
            return False
    if len(tmp) != 0:
        return False
    else:
        return True

s = "(]"
print(brace_match(s))