class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0

    def add(self, value):
        if (self.head == self.tail and self.queue[self.tail] != None):
            self.head += 1

        self.queue[self.tail] = value

        if len(self.queue) == self.tail + 1:
            self.tail = 0
        else:
            self.tail += 1

    def remove(self, count):
        for i in range(count):
            if self.head + i < len(self.queue):
                self.queue[self.head + i] = None
            else:
                self.queue[len(self.queue) - 1 - i] = None

    def getElement(self, num):
        if self.head + num < len(self.queue):
            return self.queue[self.head + num]
        else:
            return self.queue[len(self.queue) - 1 - num]
    
    def show(self):
        print(self.queue)

fifo = Queue(3)

fifo.add(0)
fifo.add(1)
fifo.add(2)
fifo.add(3)

fifo.show()

print(fifo.getElement(2))