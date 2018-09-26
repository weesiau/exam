class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,newdata):
        if newdata < self.data: # go left
            if self.left is None: # no child node
                self.left = BST(newdata)
            else:
                self.left.insert(newdata)
        else: # go right
            if self.right is None:
                self.right = BST(newdata)
            else:
                self.right.insert(newdata)

    def update(self,olddata,newdata):
        if olddata == self.data:
            
            

    def inorderdisplay(self):
        if self.left:
            self.left.inorderdisplay()
        print(self.data)
        if self.right:
            self.right.inorderdisplay()

    def preorderdisplay(self):
        print(self.data)
        if self.left:
            self.left.preorderdisplay()
        if self.right:
            self.right.preorderdisplay()

    def postorderdisplay(self):
        if self.left:
            self.left.postorderdisplay()
        if self.right:
            self.right.postorderdisplay()
        print(self.data)

#main
bst = BST('tian')
bst.insert('ben')
bst.insert('ming')
bst.insert('wei')
bst.insert('ang')
bst.insert('van')
bst.preorderdisplay()
