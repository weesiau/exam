class Node:

    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,newdata):
        n = Node(newdata)
        if self.head is None: # empty ll
            self.head = n
        else: # non empty ll
            curr = self.head
            prev = None
            while curr.link is not None and newdata > curr.data:
                prev = curr
                curr = curr.link
            if prev == None: # newdata is smallest in order
                n.link = self.head
                self.head = n
            elif curr.link is None: # newdata is largest in order
                curr.link = n
            else: # newdata is somewhere in middle of order
                n.link = curr
                prev.link = n

    def delete(self,target):
        if self.head is None:
            print('Cannot delete from empty linked list.')
            return -1
        else:
            curr = self.head
            prev = None
            while curr.link is not None and curr.data != target:
                prev = curr
                curr = curr.link
            if prev == None: #delete first node in linked list
                self.head = curr.link
            elif curr.data == target:
                prev.link = curr.link
            else:
                print('Target not found.')
                return -1

    def update(self,olddata,newdata):
        if self.delete(olddata) == -1:
            print('Value to be updated is not found.')
            return -1
        else:
            self.insert(newdata)

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.link

ll = LinkedList()
ll.insert('c')
ll.insert('a')
ll.insert('d')
ll.insert('b')
ll.display()
ll.update('d','f')
ll.display()
                
                
                
            
