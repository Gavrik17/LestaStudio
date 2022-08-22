class Queue:
    def __init__(self):
        self.queue = []
    
    def show(self):
        print(self.queue)
    
    def add(self, value):
        self.queue.append(value)

    def remove(self):
        if len(self.queue) == 0:
            return
        self.queue.pop(0)

fifo = Queue()

fifo.add(5)
fifo.add(7)
fifo.show()
fifo.remove()
fifo.show()