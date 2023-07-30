class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        pre = self.head
        temp = self.head
        if self.head == None:
            return None
        while temp is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None;
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
        
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

my_linked_list.append(5)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

my_linked_list.print_list()

my_linked_list.pop()

my_linked_list.print_list()