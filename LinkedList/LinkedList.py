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
        return
    
    def __length__(self):
        if self.head is None:
            return 0
        
        current_node = self.head
        tot = 0
        
        while current_node:
            tot += 1
            current_node = current_node.next
            
        return tot
    
    def __display__(self):
        if self.head is None:
            print('List has no element to show')
            return
        
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def __to_list__(self):
        node_data = []
        current_node = self.head
        
        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
            
        return node_data
      
    def __invert__(self):
        previous_node = None
        current_node = self.head
        
        while current_node is not None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
            
        self.head = previous_node
        
    def __get__(self, index):
        if index >= self.__length__() or index < 0:
            print('ERROR: Index out of range')
            return None
        
        current_node = self.head
        current_index = 0
        
        while current_node is not None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1
            
    def __search__(self, value):
        if self.head is None:
            print('The list has no element to search')
            return
        
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == value:
                print('Item found')
                return True
            current_node = current_node.next
            
        print('Item not found')
        return False
    
    def __remove_at_start__(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        
    def __remove_at_end__(self):
        if self.head is None:
            return
        
        current_node = self.head
        
        while current_node.next.next is not None:
            current_node = current_node.next
            
        current_node.next = None
        
    def __remove_element_by_value__(self, value):
        current_node = self.head
        
        if current_node is not None:
            if current_node.data == value:
                self.head = current_node.next
                current_node = None
                return    
    
        
        while current_node is not None:
            if current_node.data == value:
                break
            prev = current_node
            current_node = current_node.next
                
        if current_node is None:
            return
        
        prev.next = current_node.next
        current_node = None
              
    def __insert_at_start__(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
           
    def __insert_at_end__(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
            
    def __insert_at_index__(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        idx = 1
        current_node = self.head
        
        while idx < index - 1 and current_node is not None:
            current_node = current_node.next
            idx += 1
        
        if current_node is None:
            print('ERROR: Index out of Range')
        else:
            new_node = Node(data)
            new_node.next = self.head
            current_node.next = new_node
        

# :] - 'Test Here' ------------------------------------------------------------------------------------------------------------

# mylist = LinkedList()