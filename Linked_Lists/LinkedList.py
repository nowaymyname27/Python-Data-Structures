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
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None;
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp != None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.ength += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def find_middle_node(self):
        turtle = self.head
        hare = self.head
        while hare != None and hare.next != None:
            turtle = turtle.next
            hare = hare.next.next
        return turtle
    
    def has_loop(self):
        turtle = self.head
        hare = self.head
        while hare != None and hare.next != None:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                return True
        return False
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def reverse_between(self, m, n):
        if self.head == None:
            return
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next
        current = prev.next
        dist = n - m
        temp = current.next
        for _ in range(dist):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next
    
    def partition_list(self, x):
        if self.head == None or self.head.next == None:
            return
        ll1 = LinkedList(0)
        ll2 = LinkedList(0)
        ll1.make_empty()
        ll2.make_empty()
        for _ in range(self.length):
            if self.head == None:
                break
            if self.head.value < x:
                ll1.append(self.head.value)
            if self.head.value >= x:
                ll2.append(self.head.value)
            if self.head != None:
                self.head = self.head.next
        self.make_empty()
        for _ in range(ll1.length):
            self.append(ll1.head.value)
            ll1.head = ll1.head.next
        for _ in range(ll2.length):
            self.append(ll2.head.value)
            ll2.head = ll2.head.next
    
    def remove_duplicates(self):
        values = set()
        previous = Node(None)
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next
            
    def binary_to_decimal(self):
        sum = 0
        length = self.length - 1
        temp = self.head
        for _ in range(self.length):
            if temp.value == 1:
                sum += 2**(length)
            length -= 1
            temp = temp.next
        print(sum)    
            
                
            
        
            
        
    

def find_kth_from_end(list, k):
    fast = list.head
    slow = list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow 
        
        
my_linked_list = LinkedList(1)
my_linked_list.append(0)
my_linked_list.append(1)


# my_linked_list.print_list()

my_linked_list.binary_to_decimal()












