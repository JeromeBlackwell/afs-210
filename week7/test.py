class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.head = None             
        self.tail = None       
        self.count = 0
  
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
           self.head.prev = new_node
           new_node.next = self.head
           self.head = new_node

        self.count += 1

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.count += 1

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        new_node = Node(data)
        # print (index, self.count)
        if index == self.count:
            return  self.addLast(data)
        elif index >  (self.count):
              return
        elif index == 0:
                return self.addFirst(data)
            
            
        curr = self.head
        prev = self.head
        count = 0
        
        while curr!=None:
            if count == index:
                #adding
                new_node.prev = prev
                new_node.next = curr
                curr.prev = new_node
                prev.next = new_node
                self.count += 1
                break
            else:
                count += 1
                prev = curr
                curr = curr.next


    def indexOf(self, data):
            # Search through the list. Return the index position if data is found, otherwise return -1    
        curr = self.head
        pos = -1

        while curr.next !=None:
            pos +=1
            if(curr.data == data):
                return pos
            
            curr = curr.next
        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr



items = DoublyLinkedList()

items.addFirst('May')
items.add('the')
items.add('Force')
items.add('be')
items.add('with')
items.add('you')
items.add('!')
print (items)
items.addAtIndex('all',6)
items.addAtIndex('us',5)
print (items.indexOf('with'))
items.delete('you')
print (items)