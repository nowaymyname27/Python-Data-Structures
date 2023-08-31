class Node:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, value):
        """
        Initializes the Node with a given value.

        :param value: Value to be stored in the node.
        """
        self.value = value  # The value/data the node holds
        self.next = None    # Reference to the next node in the list
        self.prev = None    # Reference to the previous node in the list

class DoublyLinkedList:
    """
    Represents a doubly linked list.
    """
    def __init__(self, value):
        """
        Initializes the DoublyLinkedList with a single node of the given value.

        :param value: Value to be stored in the first node.
        """
        new_node = Node(value)   # Create a new node with the provided value
        self.head = new_node     # Set the new node as the head of the list
        self.tail = new_node     # Also set it as the tail (since it's the only node in the list)
        self.length = 1          # Set initial length of the list to 1
    
    def print_list(self):
        """
        Prints the values in the doubly linked list.
        """
        temp = self.head          # Start at the head of the list
        while temp is not None:   # Continue until reaching the end of the list
            print(temp.value)     # Print the current node's value
            temp = temp.next      # Move to the next node in the list
    
    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        :param value: Value to be stored in the new node.
        :return: True if the node is successfully appended.
        """
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty...
            self.head = new_node  # Set the new node as the head
            self.tail = new_node  # And also as the tail
        else:
            self.tail.next = new_node  # Attach new node to the end of the list
            new_node.prev = self.tail  # Set the previous reference of new node to the current tail
            self.tail = new_node       # Update the tail to the new node
        self.length += 1               # Increment the list length
        return True                    # Indicate successful append
    
    def pop(self):
        """ Removes and returns the node at the end of the list. """
        # If list is empty
        if self.length == 0:
            return None
        
        # Capture the tail node
        temp = self.tail
        
        # If only one node exists
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            # Disconnect the tail and move to the previous node
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        # Decrease the length of the list
        self.length -= 1
        
        return temp
    
    def prepend(self, value):
        """ Adds a node with the given value to the beginning of the list. """
        new_node = Node(value)
        
        # If list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect new node to the head and update head reference
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        # Increase the length of the list
        self.length += 1
        
        return True
    
    def pop_first(self):
        """ Removes and returns the node at the beginning of the list. """
        # If list is empty
        if self.length == 0:
            return None
        
        # Capture the head node
        temp = self.head
        
        # If only one node exists
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Disconnect the head and move to the next node
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        # Decrease the length of the list
        self.length -= 1
        
        return temp
    
    def get(self, index):
        """ Fetches the node at the given index. """
        # Handle index out of range
        if index < 0 or index > self.length:
            return None
        
        # If index is in the first half of the list, iterate from the head
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            # Otherwise, iterate from the tail (more efficient for second half)
            temp = self.tail
            index_from_tail = self.length - 1 - index
            for _ in range(index_from_tail):
                temp = temp.prev
        
        return temp
    
    def set(self, index, value):
        """ Updates the value of the node at the given index. """
        # Fetch the node at the specified index
        temp = self.get(index)
        if temp:
            # Update its value
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """ Inserts a new node with the given value at the specified index. """
        # Handle index out of range
        if index < 0 or index > self.length:
            return False
        # Handle edge cases of inserting at beginning or end
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        
        # Fetch nodes surrounding the desired insertion point
        before = self.get(index - 1)
        after = before.next
        
        # Create new node and connect it in between 'before' and 'after'
        new_node = Node(value)
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        # Increase the length of the list
        self.length += 1
        
        return True

    
    def remove(self, index):
        """
        Removes the node at the specified index.

        :param index: The index of the node to remove.
        :return: The removed node or False if the index is out of range.
        """
        # Handle index out of range
        if index < 0 or index > self.length:
            return False
        
        # Remove the first node if index is 0
        if index == 0:
            self.pop_first()
            return True
        
        # Remove the last node if index is at the end
        if index == self.length - 1:
            self.pop()
            return True
        
        # Get the node before the target and the target node itself
        before = self.get(index - 1)
        temp = before.next
        after = temp.next
        
        # Disconnect the target node from the list
        before.next = after
        after.prev = before
        
        temp.prev = None
        temp.next = None
        
        # Decrease the length of the list
        self.length -= 1
        
        return temp
    
    def swap_first_last(self):
        """ Swaps the values of the first and last nodes in the list. """
        # If there's only one node or none, no swap is needed
        if self.length < 2:
            return
        
        # Swap values of head and tail nodes
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
    
    def reverse(self):
        """ Reverses the list in place. """
        # If there's only one node or none, no reversal is needed
        if self.length < 2:
            return
        
        # Iterate through each node and swap the next and previous pointers
        current = self.head
        for _ in range(self.length):
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        
        # Swap head and tail pointers after reversal
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
        """
        Swaps every two adjacent nodes in the list.

        Example:
        Given 1 -> 2 -> 3 -> 4, the result will be 2 -> 1 -> 4 -> 3.
        """
        # Create a dummy node that acts as the previous node for the head of the list
        dummy = Node(0)
        dummy.next = self.head
        # Initialize previous node as dummy
        prev = dummy

        # Loop through the list while there are at least two nodes left
        while self.head and self.head.next:
            # Identify the two nodes to be swapped
            first_node = self.head
            second_node = self.head.next

            # Swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Adjust the previous pointers
            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node

            # Move the head pointer and previous node pointer for the next iteration
            self.head = first_node.next
            prev = first_node

        # Adjust the head of the list to the node after dummy
        self.head = dummy.next
        # Ensure the previous pointer of the head is set to None
        if self.head:
            self.head.prev = None

            
            
            
            
            
                
                     
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_pairs()

my_doubly_linked_list.print_list()

