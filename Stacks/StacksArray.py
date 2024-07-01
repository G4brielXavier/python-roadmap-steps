#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks using Array ============

class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0 
        
    def __push__(self, data):
        if self.next_index == len(self.arr):
            print('Out of space! Increasing array capacit...')
            self.__handle_stack_capacity_full()
            
            
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
        
    def __pop__(self):
        if self.is_empty():
            self.next_index = 0 
            return None
        
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]
    
    def __size__(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
    
    def __handle_stack_capacity_full__(self):
        old_arr = self.arr
        
        self.arr = [0 for _ in range(2*len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
            
#:] - 'Test here' ----------------------------------------------------