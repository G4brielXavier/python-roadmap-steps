#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks using Linked List ============

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class StackWithLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def __is_empty__(self):
        return self.size == 0
    
    def __push__(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def __pop__(self):
        if self.__is_empty__():
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data


# :] - 'Test here' -------------------------------------------------------------------