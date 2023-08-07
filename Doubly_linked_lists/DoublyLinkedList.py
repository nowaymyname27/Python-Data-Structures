class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            last_index_number = self.length - 1
            index_from_tail = last_index_number - index
            for _ in range(index_from_tail):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        before = self.get(index - 1)
        after = before.next
        new_node = Node(value)
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        before = self.get(index - 1)
        temp = before.next
        after = temp.next
        
        before.next = after
        after.prev = before
        
        temp.prev = None
        temp.next = None
        
        self.length -= 1
        return temp
    
    def swap_first_last(self):
        if self.length < 2:
            return
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
    
    
    def reverse(self):
        if self.length < 2:
            return       
        current = self.head
        temp = current.next
        for _ in range(self.length):
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp 
        
    def is_palindrome(self):
        # If the length of the list is 0 or 1, it is always a palindrome
        if self.length <= 1:
            return True
        
        # Create two pointers, one starting from the head and the other from the tail
        forward_node = self.head
        backward_node = self.tail
        
        # Iterate over half of the list
        for i in range(self.length // 2):
            # If the values at the two ends of the list do not match, the list is not a palindrome
            if forward_node.value != backward_node.value:
                return False
            
            # Move the two pointers towards each other
            forward_node = forward_node.next
            backward_node = backward_node.prev
        
        # If all values matched, the list is a palindrome
        return True
    
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
                
            self.head = first_node.next
            prev = first_node
        self.head = dummy.next
        if self.head:
            self.head.prev = None
            
            
            
            
            
                
                     
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_pairs()

my_doubly_linked_list.print_list()

