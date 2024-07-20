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
from SearchBinareTree.BST import TreeNode

root = TreeNode(10)
root.__insert__(5, 'data1')
root.__insert__(14, 'data2')
root.__insert__(3, 'data3')
root.__insert__(2, 'data4')
root.__insert__(12, 'data5')
root.__insert__(16, 'data6')

print(root.__find__(12))