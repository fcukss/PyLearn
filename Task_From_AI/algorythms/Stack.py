"""in python list is STACK
"""


"""Valid Parentheses (Правильные скобки)
LeetCode №20"""

def isValid(s:str)-> bool:
    stack = []
    #Создаем словарь, где ключи — закрывающие скобки, а значения — открывающие:
    mapping = {')':'(',
               '}':'{',
               ']':'['}
    for c in s:
        if c in mapping:
            top_el  = stack.pop() if stack else '!'
            if mapping[c] != top_el:
                return False
        else:
            stack.append(c)
    return not stack


"""var2"""


def isValid2(s:str)-> bool:
    stack = []
    mapping = {')':'(',
               '}':'{',
               ']':'['}
    for c in s:
        if c in mapping.values():
            stack.append(c)
        else:
            if not stack or stack[-1] !=mapping[c]:
                return False
            stack.pop()
    return len(stack)==0

"""var3"""
def isValidNoDict(s: str) -> bool:
    stack = []
    for c in s:
        # Если открывающая — кладем в стек
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            # Если закрывающая, а стек пуст — сразу ошибка
            if not stack:
                return False

            # Достаем последнюю открытую скобку
            last = stack.pop()

            # Проверяем соответствие вручную
            if c == ')' and last != '(':
                return False
            if c == '}' and last != '{':
                return False
            if c == ']' and last != '[':
                return False

    return len(stack) == 0

s = "()[]{}"
s1 = '([)]'
s2 = '((()))'

print(isValid(s))
print(isValid(s1))
print(isValid(s2))

print(isValid2(s))
print(isValid2(s1))
print(isValid2(s2))


print("------------------------------------")
"""155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
           val = min(self.min_stack[-1],val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

print("____________________________________________")
"""Daily Temperatures (Ежедневные температуры)
LeetCode №739
"""
def daily_Temperatures(temperatures: list[int])-> list[int]:
    res = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        current_tem = temperatures[i]
        while stack and current_tem > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res



temps = [10, 12, 15, 11, 9, 13,20]
current_res = daily_Temperatures(temps)

res = [1, 1, 4, 2, 1, 1, 0]

if current_res == res:
    print(current_res)
    print(True)
else:
    print(current_res)
    print(False)