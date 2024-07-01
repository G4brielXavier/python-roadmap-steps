#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues using Stacks ============

from Stacks.Stacks import Stacks

class Queues:
    def __init__(self):
        self.instorage = Stacks()
        self.outstorage = Stacks()
        
    def __length__(self):
        return self.instorage.__length__() + self.outstorage.__length__()
    
    def __enqueue__(self, data):
        self.instorage.__push__(data)
        
    def __dequeue__(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.__push__(self.instorage.__pop__())
        return self.outstorage.__pop__()
    
# :] - 'Test here' -----------------------------------------------------------------