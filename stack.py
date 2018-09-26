class Stack:

    MAX = 5 # stack holds MAX number of items

    def __init__(self):
        self.data = []
        for i in range(self.MAX):
            self.data.append(0) # initialise stack with dummy values
        self.top = -1

    def is_full(self):
        return self.top == self.MAX - 1

    def is_empty(self):
        return self.top == -1

    def push(self,newdata):
        if self.is_full():
            print('Cannot insert to full stack.')
        else:
            self.top += 1
            self.data[self.top] = newdata

    def pop(self):
        if self.is_empty():
            print('Cannot remove from empty stack.')
        else:
            result = self.data[self.top]
            self.top -= 1
            return result

    def peek(self):
        if self.is_empty():
            print('Empty stack.')
        else:
            print(self.data[self.top])

    def display(self):
        if self.is_empty():
            print('Empty stack.')
        else:
            for i in range(self.top+1):
                print(self.data[i])

#main
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.push('e')
s.display()
s.pop()
s.display()
