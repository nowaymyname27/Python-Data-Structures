class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        else:
            return self.stack_list.pop()
        

def is_balanced_parentheses(string):
    parentheses_stack = Stack()
    for i in range(len(string)):
        if string[i] == "(":
            parentheses_stack.push("(")
        if string[i] == ")":
            par = parentheses_stack.pop()
            if par == None:
                return False
    if parentheses_stack.peek() is not None:
        return False
    return True
    
is_balanced_parentheses("(((as)))(")