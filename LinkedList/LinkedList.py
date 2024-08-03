#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Practice LinkedLists ============

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __append__(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
        
    def __len__(self):
        if self.head is None:
            return 0
        
        len_number = 0
        current_node = self.head
        
        while current_node:
            len_number += 1
            current_node = current_node.next
            
        return len_number
    
    def __to_list__(self):
        node_data = []
        current_node = self.head
        
        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
            
        return node_data
    
    def __get__(self, index):
        if index >= self.__len__() or index < 0:
            print('ERROR: Index out of range')
            return
        
        current_index = 0
        current_node = self.head
        
        while current_node is not None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1
            
    def __invert__(self):
        previous_node = None
        current_node = self.head
        
        while current_node is not None:
            next = current_node.next
            current_node.next = previous_node
            prev = current_node
            current_node = next
            
        self.head = previous_node
        
    def __search__(self, data):
        if self.head is None:
            print('List has no element')
            return
        
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                print('Founded')
                return True
            current_node = current_node.next
            
        print('Not founded')
        return False
      
      
    def __display__(self):
        if self.head is None:
            print('List has no elements to show')
            return
        
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def remove_at_start(self):
        if self.head is None:
            print('List has no element')
            return
        
        self.head = self.head.next
        
    def remove_at_end(self):
        if self.head is None:
            print('List has no element')
            return
        
        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next
            
    def remove_element_by_data(self, data):
        current_node = self.head
        
        if current_node is not None:
            if current_node.data == data:
                self.head = current_node.next
                current_node = None
                return
            
        while current_node is not None:
            if current_node.data == data:
                break 
            prev = current_node
            current_node = current_node.next
            
        if current_node is None:
            return
        
        prev.next = current_node.next
        current_node = None
        
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        
        while current_node is not None:
            current_node = current_node.next
            
        current_node = new_node
        
        
    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
        i = 1
        current_node = self.head
        
        while i < index-1 and current_node is not None:
            current_node = current_node.next
            i += 1
            
        if current_node is None:
            print('ERROR: Index out of range')
        else:
            new_node = Node(data)
            self.head = current_node.next
            current_node.next = new_node
            

            
# :] - 'Test Here' ------------------------------------------------------------------------------------------------------------
