#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues using Stacks ============

class Stacks:
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def __push__(self, data):
        self.items.append(data)
        
    def __pop__(self):
        if self.__len__() == 0:
            return None
        
        self.items.pop()

class QueuesWithStacks:
    def __init__(self):
        self.instorage = Stacks()
        self.outstorage = Stacks()
        
    def __len__(self):
        return self.instorage.__len__() + self.outstorage.__len__()
    
    def __enqueue__(self, data):
        self.instorage.__push__(data)
        
    def __dequeue__(self):
        if self.__len__() == 0:
            return None
        
        self.outstorage.__push__(self.instorage.__pop__())
            
# :] - 'Test here' -----------------------------------------------------------------

q = QueuesWithStacks()

for i in range(1, 10+1):
    q.__enqueue__(i)
    
for i in range(1, 5):
    q.__dequeue__()
    
print(q.instorage.items)
print(q.outstorage.items)