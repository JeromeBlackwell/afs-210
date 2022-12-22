class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None





class stack:
    def __init__(self):
            self.data = []

    def push(self, data ):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if len(self.data) == 0:
            return False
        else:
            return True   
    def peek (self):
        return self.data[len(self.data) -1]

# stack = stack()
# stack.push(10)
# print(stack.peek())
# answer = stack.pop()
# print(answer)



class queue:
    def _init_(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data ):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.count += 1
  
    def dequeue(self):
        curr = self.head.next
        curr.prev = None
        self.head = curr
        
    def size(self):
        return self.count 

    def isEmpty(self):
        if self.count == 0:
            return False
        else:
            return True
        

    def peek (self):
        return self.head
    


# queue.push()
# print(queue.peek())
# answer = queue.pop()
# print(answer)

def isPalindrome (str):
    new_queue = queue()
    new_stack = stack()
    print(str)

monster = input ('Enter string of choice: ')
print (isPalindrome(monster))
