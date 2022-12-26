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
        return self.data[-1]

    def __str__(self):
        return str(self.data)




class queue:
    def __init__(self):
        self.data = []
        
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if len(self.data) == 0:
            return False
        else:
            return True

    def enqueue(self,data):
        self.data.insert(0,data)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def __str__(self):
        return str(self.data)



def isPalindrome (str):
    new_queue = queue()
    new_stack = stack()
    
    for letter in str:
        new_queue.enqueue(letter)
        new_stack.push(letter)

    print(new_queue)
    print(new_stack)

monster = input ('Enter string of choice: ')
isPalindrome(monster)






    


