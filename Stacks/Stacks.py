#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks ============

class Stacks:
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def __add__(self, data):
        self.items.append(data)
        
    def __pop__(self, data):
        if self.__len__() == 0:
            return
        
        self.items.pop()
            
            
# :] - 'Test Here' -----------------------------------------------------------------------      