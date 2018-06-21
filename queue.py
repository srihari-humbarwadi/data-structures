# Linked list implementation
# author Srihari Humbarwadi
# Date 23/06/2018


class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def Size(self):
        return len(self.queue)

    def Display(self):
        for x in self.queue:
            print(x, "", end="")
        print("")


q = Queue()
print(q.isEmpty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.Display()
q.dequeue()
q.Display()
q.dequeue()
q.Display()
