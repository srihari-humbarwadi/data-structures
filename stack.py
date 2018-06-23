# Stack implementation
# author Srihari Humbarwadi
# Date 13/06/2018


class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        if len(self.stack) == 0:
            return
        return self.stack[-1]

    def Size(self):
        return len(self.stack)

    def Display(self):
        for x in self.stack:
            print(x, "", end="")
        print("")


sa = Stack()
sa.push(10)
sa.push(20)
sa.push(30)
sa.push(40)
sa.push(50)
sa.Display()
print(sa.pop())
print(sa.pop())
sa.Display()
print(sa.peek())
print(sa.Size())

