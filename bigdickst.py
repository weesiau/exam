class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,newdata):
        if newdata < self.data:
            if self.left is None:
                self.left = BST(newdata)
            else:
                self.left.insert(newdata)
        else:
            if self.right is None:
                self.right = BST(newdata)
            else:
                self.right.insert(newdata)

    def search(self,target):
        if self.data == target: # found
            return 'Found'
        elif self.left is None and self.right is None:
            return 'Not Found'
        elif target < self.data: # search left
            if self.left is None:
                return 'Not Found'
            else:
                return self.left.search(target)
        else: # search right
            if self.right is None:
                return 'Not Found'
            else:
                return self.right.search(target)

    def lookup(self,target,parent = None):
        if self.data == target: #target found, return node and parent (nodes)
            return self,parent
        elif self.left is None and self.right is None:
            return None,None
        elif target < self.data:
            if self.left is None:
                return None,None
            else:
                return self.left.lookup(target,self)
        else:
            if self.right is None:
                return None,None
            else:
                return self.right.lookup(target,self)

    def delete(self,target):
        if self.search(target) == 'Not Found':
            return 'Not Found'
        else:
            node,parent = self.lookup(target)
            if node.left is None and node.right is None: #target node has 0 children
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif (node.left is None) != (node.right is None): #target node has 1 child
                if node.left: #1 child is left
                    n = node.left
                else: #1 child is right
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
            else: #target node has 2 children, replace with inorder successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                #replace with inorder successor
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
