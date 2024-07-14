#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues ============

class Queues:
    def __init__(self):
        self.queue = []
        
    def __len__(self):
        return len(self.queue)
    
    def __push__(self, data):
        self.queue.append(data)
        
    def __pop__(self):
        if self.__len__():
            return
        
        self.queue.pop()
            
# :] - 'Test here' -------------------------------------------------