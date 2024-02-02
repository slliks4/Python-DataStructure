# Creating a LinkedList

class LinkedList:
    class _Node:
        def __init__(self, item = None, nextNode = None) -> None:
            self._item = item # creating the item in the node
            self._nextNode = nextNode # creating the link to the next node

    def __init__(self) -> None:
        self._first = None # The first node in the linked list

    # Add a node to the linked list
    def insert(self, newItem):
        # First will be overwritten by the new node and the link will be the first node i.e current node
        self._first = self._Node(newItem, self._first) 

    def delete(self):
        item =  None # incase there is no item in the linked list
        if self._first is not None:
            item =  self._first._item # Reference to the first node in the linked list
            self._first = self._first._nextNode

        return item
    
    def __iter__(self):
        counter = self._first
        while counter is not None:
            yield counter._item
            counter = counter._nextNode

def unwind(node):
    if node._nextNode is not None: # traverse up to the head
        unwind(node._nextNode)

    if node._item is not None:
        print (node._item)

            
def main():
    l = LinkedList()

    for i in range(13): l.insert(f"node{i}")

    print("list in order of first to last")
    for i in l : print(i)
    print("\nList in reverse order:")
    unwind(l._first)

if __name__ == "__main__":
    main()