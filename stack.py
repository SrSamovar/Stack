class Stack:
    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack = self.stack.append(item)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError('Извлекается из пустой стопки')

    def peek(self):
        self.stack.peek()

    def size(self):
        return len(self.stack)


def is_balanced(test):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    matching = {')': '(', ']': '[', '}': '{'}

    for char in test:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matching[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    test = input("Введите строку со скобками:")
    result = is_balanced(test)
    print(result)
