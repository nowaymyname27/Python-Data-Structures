class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
        
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
        
            
my_BST = Binary_Search_Tree()

my_BST.insert(47)
my_BST.insert(21)
my_BST.insert(76)
my_BST.insert(18)
my_BST.insert(27)
my_BST.insert(52)
my_BST.insert(82)

print(my_BST.r_contains(27))
print(my_BST.r_contains(17))
        