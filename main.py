
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) > 0:
            return True
        return False

    def check(self, element):
        is_good = True
        for i in element:
            if i in '([{':
                self.stack.append(i)
            if i in ')]}':
                if not self.stack:
                    is_good = False
                else:
                    open_bracket = self.stack.pop()
                if open_bracket == '(' and i == ')' \
                        or open_bracket == '[' and i == ']' \
                        or open_bracket == '{' and i == '}':
                    continue
                is_good = False
                break


        if is_good:
            return 'Сбаланировано'
        else:
            self.stack.clear()
            return 'Несбалансировано'

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            self.stack.pop()
            try:
                return self.stack[-1]
            except IndexError:
                print('Nothing to return')
        else:
            return 'The stack is empty'

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


new_stack = Stack()
print(new_stack.check('(d)a)'))
new_stack.push('(([]))')
new_stack.push('(([po))')
new_stack.push('(([]))')
print(new_stack.pop())
print(new_stack.peek())
print(new_stack.size())
