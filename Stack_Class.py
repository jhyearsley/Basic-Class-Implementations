# Stack Class

class Stack(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self,val):
        self.item.append(val)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)


def rev_string(string):
    string_stack = Stack()
    [string_stack.push(i) for i in string]

    reversed_string = ''
    while not string_stack.is_empty():
        reversed_string += string_stack.pop()

    return reversed_string


def dec_to_binary(num):
    remainder_stack = Stack()

    while num > 0:
        remainder_stack.push(num % 2)
        num /= 2

    binary = ''

    while not remainder_stack.is_empty():
        binary += str(remainder_stack.pop())

    
    return binary

def infix_to_postfix(expression):
    OPERANDS = 'ABCDEFGHIKJLMNOPQRSTUVWXYZ0123456789'
    OPERATORS = '*/+-'
    op_stack = Stack()
    output = []
    precedence = {}
    precedence['('] = 1
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2

    expressions = [i for i in expression]

    for val in expressions:
        if val in OPERANDS:
            output.append(val)

        elif val == '(':
            op_stack.push(val)

        elif val == ')':
            while op_stack.peek() is not '(':
                output.append(op_stack.pop())
            op_stack.pop()

        else:            
            while not op_stack.is_empty() and (
                precedence[val] <= precedence[op_stack.peek()]):
                output.append(op_stack.pop())

            op_stack.push(val)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return ''.join(output)
            
    
    
