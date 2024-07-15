#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks ============

class Stacks:
    def __init__(self):
        self.items = []
        
    def __length__(self):
        return len(self.items)
    
    def __push__(self, data):
        self.items.append(data)
        
    def __pop__(self):
        if self.__length__() == 0:
            return None
        
        self.items.pop()
            
    def __display__(self):
        it = self.items
        
        for i in it:
            print(i)
            
# :] - 'Test Here' -----------------------------------------------------------------------      