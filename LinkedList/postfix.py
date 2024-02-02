from linkedstack import *

# compute value of postfix expression using a stack
def postfix(expr):
    s = Stack()
    for term in expr:
        if isinstance(term, int or float): s.push(term)
        else:
            b = s.pop()
            a = s.pop()
            s.push(calc(a, b, term))

    return s.pop()
    
# helper method performs an arithmetic operation
def calc(a, b, op):
    if op == '+':   return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b

def main():
    print(postfix([9, 1, '-', 2, '/']))

if __name__ == '__main__':
    main()
