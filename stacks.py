stack = []

stack.append('A')
stack.append('B')
stack.append('C')

print("Stack: ", stack)

top_element = stack[-1]
print("Top element : ", top_element)

popped_element = stack.pop()
print("Popped element : ", popped_element)

print("Stack after popping: ", stack)
print("isEmpty: ", not bool(stack))
print("Size: ", len(stack))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            print("Empty Stack")
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():
            print("Empty Stack")
        return self.stack[-1]


mystack = Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')

print('Stack:', mystack.stack)
print('Pop: ', mystack.pop())
print('Stack after pop: ', mystack.stack)
print('Peek', mystack.peek())
print('Size: ', mystack.size())
print('Is empty: ', mystack.isEmpty())