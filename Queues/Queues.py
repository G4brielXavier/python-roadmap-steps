#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues ============

class Queue:
    def __init__(self):
        self.queues = []
        
    def __length__(self):
        return len(self.queues)
    
    def __push__(self, data):
        self.queues.append(data)
        
    def __pop__(self):
        if self.__length__() == 0:
            return None
        else:
            self.queues.pop()
            
            
# :] - 'Test here' -------------------------------------------------