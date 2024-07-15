#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues using LinkedList ============

from LinkedList.LinkedList import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __enqueue__(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        
    def __length__(self):
        return self.length
    
    def __dequeue__(self):
        if self.__length__() == 0:
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
    
    
# :] - 'Test here' -------------------------------------------------------------------