class Node:

    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def size(self):
        totalsize = 0
        curr = self.head
        while curr is not None:
            totalsize += 1
            curr = curr.link
        return totalsize

    def insert(self,newdata,position = 0):
        n = Node(newdata)
        if self.head is None:
            self.head = n
        else:
            if position == 0: # insert in front
                n.link = self.head
                self.head = n
            elif position == self.size(): # insert at back
                curr = self.head
                while curr.link is not None:
                    curr = curr.link
                curr.link = n
            else: # insert in middle
                curr = self.head
                temp = None
                for i in range(position - 1):
                    temp = curr
                    curr = curr.link
                if temp == None:
                    n.link = curr.link
                    curr.link = n
                else:
                    n.link = curr
                    temp.link = n

    def delete(self,target):
        curr = self.head
        temp = None
        if curr.data == target: # target is in first node
            self.head = curr.link
            return
        else:
            while curr.link is not None:
                temp = curr
                curr = curr.link
                if curr.data == target:
                    temp.link = curr.link
                    return
            print('Target not found')
            return

    def update(self,olddata,newdata):
        curr = self.head
        temp = None
        n = Node(newdata)
        if curr.data == olddata: # target is in first node
            n.link = curr
            self.head = n
            return
        else:
            while curr.link is not None:
                temp = curr
                curr = curr.link
                if curr.data == olddata:
                    n.link = curr.link
                    temp.link = n
                    return
            print('Target not found')
            return

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.link

ll = LinkedList()
ll.insert('hi')
ll.insert('suck',ll.size())
ll.insert('you',1)
ll.display()
ll.update('you','i')
ll.display()
                
        
