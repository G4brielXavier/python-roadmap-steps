#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Search in binare tree ============

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def search(node, target):
    if node is None:
        return None
    
    if node.data == target:
        return node 
    elif node.data > target:
        return search(node.right, target)
    elif node.data < target:
        return search(node.left, target)
    
root = TreeNode(15)    

node5 = TreeNode(5)
node9 = TreeNode(9)
node12 = TreeNode(12)
node10 = TreeNode(10)
node3 = TreeNode(3)
node18 = TreeNode(18)
node16 = TreeNode(16)

root.left = node5 
root.right = node9

node5.left = node3
node5.right = node9

node9.left = node5
node9.right = node10

node16.left = node12
node16.right = node18

node18.left = node16

result = search(root, 18)


if result:
    print(f'Found the node with value {result.data} in BST.')
else:
    print('The value not found in BST.')