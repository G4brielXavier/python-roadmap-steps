#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks using Linked List ============

from LinkedList.LinkedList import Node

class Stacks:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __push__(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def __pop__(self):
        if self.size == 0:
            return
        
        value = self.head.data
        self.head = self.head.next
        self.size += 1
        return value
    
# :] - 'Test here' -------------------------------------------------------------------