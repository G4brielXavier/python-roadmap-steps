#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice Queues with Arrays ============

class QueuesWithArrays:
    def __init__(self, default_size=10):
        self.arr = [0 for _ in range(default_size)]
        self.num_elements = 0
        self.next_index = 0 
        
    def __len__(self):
        return self.num_elements

    def __empty__(self):
        return self.num_elements == 0
    
    def __enqueue__(self, data):
        self.arr[self.next_index] = data  
        self.next_index += 1
        self.num_elements += 1      
        
    def __dequeue__(self):
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]
    
    def __increaser__(self):
        temp_arr = self.arr
        
        self.arr = [0 for _ in range(2*len(temp_arr))]
        for i, v in enumerate(temp_arr):
            self.arr[i] = v
            
# :] - Test here -----------------------------------