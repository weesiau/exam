class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

    def insert(self,newdata):
        if newdata < self.data: #go left
            if self.left is None:
                self.left = BST(newdata)
            else:
                self.left.insert(newdata)
        else: #go right
            if self.right is None:
                self.right = BST(newdata)
            else:
                self.right.insert(newdata)

    def search(self,target):
        if self.data == target: #found
            return 'Found'
        elif self.left is None and self.right is None: #not found
            return 'Not found'
        elif target < self.data: #go left
            if self.left is None:
                return 'Not found'
            else:
                return self.left.search(target)
        else: # go right
            if self.right is None:
                return 'Not found'
            else:
                return self.right.search(target)

    def lookup(self,target,parent = None):
        if self.data == target:
            return self,parent # returns the node and its parent node
        elif self.left is None and self.right is None:
            return None, None
        elif target < self.data: # go left
            if self.left is None:
                return None, None
            else:
                return self.left.lookup(target,self)
        else: # go right
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(target,self)

    
        
