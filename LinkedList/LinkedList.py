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
    
    def __len__(self):
        if self.head is None:
            return 0
        
        tot = 0
        current_node = self.head
        
        while current_node:
            tot += 1
            current_node = current_node.next 
            
        return tot
    
    def __to_list__(self):
        node_data = []
        
        current_node = self.head
        
        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        
        return node_data    
    
    def __show__(self):
        if self.head is None:
            print('The list has no element to show')
            return None
        
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def __invert__(self):
        previous_node = None
        current_node = self.head
        
        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
            
        self.head = previous_node

    def __get__(self, index):
        if index >= self.__len__() or index < 0:
            print('ERROR: Index out of range')
            
        current_index = 0
        current_node = self.head
        
        while current_node != None:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next
            
    def __search__(self, data):
        if self.head is None:
            print('List has no element')
            return
        
        current_node = self.head
        while current_node != None:
            if current_node.data == data:
                print('Element founded')
                return True
            current_node = current_node.next
            
        print('Element not found')
        return False
    
    def __remove_at_start__(self):
        if self.head is None:
            print('The list has no element to remove')
            return
        
        self.head = self.head.next
    
    def __remove_at_end__(self):
        if self.head is None:
            print('The list has no elements to remove')
            return 
        
        current_node = self.head
        
        while current_node.next.next != None:
            current_node = current_node.next
            
        current_node.next = None

    def __remove_element_by_value__(self, data):
        current_node = self.head

        if current_node != None:
            if current_node.data == data:
                self.head = current_node.next
                current_node = None
                return
            
        while current_node != None:
            if current_node.data == data:
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
        
        while current_node.next != None:
            current_node = current_node.next
            
        current_node.next = new_node

    def __insert_at_index__(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
        id = 0
        current_node = self.head
        
        while id < index - 1 and current_node != None:
            current_node = current_node.next
            id += 1
            
            if current_node is None:
                print('ERROR: Index out of range')
            else:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
            
# :] - 'Test Here' ------------------------------------------------------------------------------------------------------------

mylist = LinkedList()

for i in range(1, 10+1):
    mylist.__append__(i)

mylist.__insert_at_index__(4, 100)
mylist.__show__()


print(f'Length: {mylist.__len__()}')