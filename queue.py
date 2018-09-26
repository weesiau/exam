class Queue: #FIFO LILO

    MAX = 5 # queue holds MAX - 1 items

    def __init__(self):
        self.data = []
        for i in range(self.MAX):
            self.data.append(0)
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.size() == self.MAX - 1

    def size(self):
        if self.front < self.rear: # no wraparound
            return self.rear - self.front
        else: # wraparound
            return self.rear + self.MAX - self.front

    def enqueue(self,newdata):
        if self.is_full():
            print('Cannot insert to full queue.')
        else:
            self.data[self.rear] = newdata
            self.rear = (self.rear + 1) % self.MAX

    def dequeue(self):
        if self.is_empty():
            print('Cannot remove from empty queue.')
        else:
            result = self.data[self.front]
            self.front = (self.front + 1) % self.MAX
            return result

    def display(self):
        if self.is_empty():
            print('Empty queue.')
        else:
            if self.front < self.rear:
                for i in range(self.front,self.rear):
                    print(self.data[i])
            else:
                for i in range(self.front,self.MAX):
                    print(self.data[i])
                for i in range(self.rear):
                    print(self.data[i])

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')
q.enqueue('e')
q.display()
q.dequeue()
q.display()
