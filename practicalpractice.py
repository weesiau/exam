class Node:

    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,newdata):
        if self.head is None:
            n = Node(newdata)
            self.head = n
        else:
            curr = self.head
            temp = None
            while curr is not None and newdata > curr.data:
                temp = curr
                curr = curr.link
            n = Node(newdata)
            if curr is None:
                temp.link = n
            else:
                if temp is None: #no movement down linked list
                    n.link = self.head
                    self.head = n
                else:
                    temp.link = n
                    n.link = curr


    def delete(self,target):
        curr = self.head
        temp = None
        while curr is not None:
            #check if curr is holding olddata
            if curr.data == target: #found, delete olddata
                if temp is None: #olddata is self.head
                    self.head = curr.link
                else:
                    temp.link = curr.link
                return
            else:
                temp = curr
                curr = curr.link

    def update(self,olddata,newdata):
        self.delete(olddata)
        self.insert(newdata)
                
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.link

ll = LinkedList()
ll.insert('Smith')
ll.insert('Wu')
ll.insert('Arma')
ll.insert('Hon')
ll.display()
ll.delete('Smith')
ll.display()
