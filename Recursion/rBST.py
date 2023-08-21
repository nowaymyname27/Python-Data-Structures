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
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def _r_contains(self, current_node, value):
        
            
my_BST = Binary_Search_Tree()

my_BST.insert(47)
my_BST.insert(21)
my_BST.insert(76)
my_BST.insert(18)
my_BST.insert(27)
my_BST.insert(52)
my_BST.insert(82)

print(my_BST.contains(27))
print(my_BST.contains(17))
        