#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Search in binare tree ============

#Pre-Order Transversal
#In-Order Transversal
#Pos-Order Transversal

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.contents = None
        self.left = None
        self.right = None
    
    def __insert__(self, data, contents=None):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
                self.contents = contents
            else:
                self.left.__insert__(data, contents)
        else:
            if self.right is None:
                self.right = TreeNode(data)
                self.contents = contents
            else:
                self.right.__insert__(data, contents)
        
    def __find__(self, data):
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.__find__(data)
        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.__find__(data)
        else:
            return self
        
    def inorder_transversal(self):
        if self.left:
            self.left.inorder_transversal()
        print(self.data)
        if self.right:
            self.right.inorder_transversal()
            
    def preorder_transversal(self):
        print(self.data)
        if self.left:
            self.left.preorder_transversal()
        if self.right:
            self.right.preorder_transversal()
        
    def posorder_transversal(self):
        if self.left:
            self.left.posorder_transversal()
        if self.right:
            self.right.posorder_transversal()
        print(self.data)
        
root = TreeNode(10)
root.__insert__(5, {'name':'Gabriel', 'age':18})
root.__insert__(14, {'name':'Lucas', 'age':20})
root.__insert__(17, {'name':'Mateus', 'age':19})
root.__insert__(2, {'name':'Carlos', 'age':18})
root.__insert__(1, {'name':'Eduardo', 'age':23})
root.__insert__(15, {'name':'Roberto', 'age':18})

print(root.__find__(5).contents['name'])      