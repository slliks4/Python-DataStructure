# A Stack object is a last-in-first-out collection.
# Implemented here as a linked-list of Node objects
class Stack:
    class _Node:  # private nested class
        def __init__(self, item = None, nextNode = None):
            self._nextNode = nextNode
            self._item = item

    # Construct an empty Stack object.
    def __init__(self):
        self._first = None  # Reference to first _Node

    # Return True if stack is empty, False otherwise. 
    def isEmpty(self):
        return self._first is None

    # Push item onto the top of stack.
    def push(self, item):
        self._first = self._Node(item, self._first)

    # Pop the top item from the stack and return it.
    def pop(self):
        if self._first is None:
            return None
        else:
            item = self._first._item
            self._first = self._first._nextNode
            return item

    # Return a string representation of stack. (Not in the API.)
    def __str__(self):
        s = ""
        cur = self._first
        while cur is not None:
            s += str(cur._item) + ", "
            cur = cur._nextNode
        return s[0:-2]

# test client
def main():
    s = Stack()
    for i in range(13): s.push(i)
    
    print("Stack contents:")
    print(str(s))
    
    s.push(20)
    print("Stack contents:")
    print(str(s))
    
    print("Removed:",str(s.pop()))
    print("Removed:",str(s.pop()))
    
    print("Stack contents:")
    print(str(s))

def reverse(input):
    s = Stack()
    for character in input:
        s.push(character)
    while (not s.isEmpty()):
        print(s.pop(), end = "")
    print("\r")


main()
reverse('reverse')


# two stacks to make a queue
def stackyqueue(list):
    s1 = Stack()
    s2 = Stack()
    for item in list:
        # keep adding items to the first stack
        if item != "*":
            s1.push(item)
        # ...until see a dequeue command
        else:
            # then move everything from first stack to second
            # which reverses the order to put the first item at the top
            while not s1.isEmpty():
                s2.push(s1.pop())
            # get that first item and display it
            print(s2.pop())
            # and move everything back onto first stack
            # which puts te first item back at the bottom
            while not s2.isEmpty():
                s1.push(s2.pop())

def main():
    stackyqueue(["a","b","c","*","d","*","*","e","*","*"])
    
if __name__ == '__main__':
    main()