#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Stacks using Array ============

class StacksWithArray:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.num_element = 0
        self.next_index = 0
        
    def __len__(self):
        return self.num_element
    
    def __is_empty__(self):
        return self.num_element == 0
    
    def __increaser__(self):
        temp_arr = self.arr 
        
        self.arr = [0 for _ in range(2*len(temp_arr))]
        for i, el in enumerate(temp_arr):
            self.arr[i] = el
    
    def __push__(self, data):
        if self.next_index > len(self.arr):
            print('In Limit, Increasing capacity...')
            self.__increaser__()
            
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_element += 1
    
    def __pop__(self):
        if self.__is_empty__():
            self.next_index = 0
            return
        
        self.next_index -= 1
        self.num_element -= 1
        return self.arr[self.next_index]    

#:] - 'Test here' ----------------------------------------------------