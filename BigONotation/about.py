#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Big O Notations ============

# Big O Notation é uma forma de saber o tempo de execução de algoritimo, e descobrir a melhor opção, para se ter um codígo relativamente rápido

# O(1) -> Constante
def hello(arr):
    print(arr[2])

# hello([2, 4, 8, 1]) - O(1)
    
# O(n) -> Onde n é quantidade de vezes (Crescimento Linear)
def ThirdElement(arr):
    for i in range(len(arr)):
        if i == 3:
            print(arr[i], end=' ')
            

# O(log(n)) -> 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __insert__(self, data):
        if data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.__insert__(data)
        else:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.__insert__(data)
                
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
            return True

root = TreeNode(10)
root.__insert__(5)
root.__insert__(6)
root.__insert__(12)
root.__insert__(2)
root.__insert__(7)

print(root.__find__(20))

# O(n log(n))
# O(n²)
# O(2 n²)