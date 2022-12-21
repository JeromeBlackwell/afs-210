class stack:
    def __init__(self):
            self._data = ['racer', 'noon', 'python', 'madam']

    def push(self, data ):
        self._data.append(data)
    

    def pop(self):
        return self._data.pop()
    def peek (self):
        return self._data[len(self._data) -1]

stack = stack()
stack.push(10)
print(stack.peek())
answer = stack.pop()
print(answer)



class queue:
    def _init_(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, data ):
        self._data.append(data)
    

    def pop(self):
        return self._data.pop()
    def peek (self):
        return self._data[len(self._data) -1]

# queue = queue()
# # queue.push()
# print(queue.peek())
# answer = queue.pop()
# print(answer)
