#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks using Array ============

class StacksWithArray:
    def __init__(self, init_size=10):
        self.arr = [0 for _ in range(init_size)]
        self.elements = 0
        self.next_index = 0
        
    def __ele__(self):
        return self.elements
    
    def __is_empty__(self):
        return self.elements == 0
    
    def __increase_capacity__(self):
        old_arr = self.arr
        
        self.arr = [0 for _ in range(len(old_arr) * 2)]
        for i, v in enumerate(old_arr):
            self.arr[i] = v
            
    def __push__(self, data):
        if self.next_index == len(self.arr):
            print('Out of space! Increasing the capacity...')
            self.__increase_capacity__()
            
        self.arr[self.next_index] = data
        self.next_index += 1
        self.elements += 1 
        
    def __pop__(self):
        if self.__is_empty__():
            self.next_index = 0
            return
        
        self.next_index -= 1
        self.elements -= 1
        return self.arr[self.next_index]
    
#:] - 'Test here' ----------------------------------------------------

starr = StacksWithArray()
b = [0 for _ in range(10)]

print('Pass' if starr.arr == b else 'Fail')