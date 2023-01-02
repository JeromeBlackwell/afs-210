class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size # will hold keys
        self.data = [None] * self.size # will hold values

    def hashfunction(self,key):
        # Insert your hashing function code
        # Key moulus table_size
        return key % self.size
    
    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self,key,data):
        # Insert your code here to store key and data
        # key = 5
        # key = "apple"
        # key = 3.13
        hashvalue = self.hashfunction(key)
        # print(hashvalue) #0..9
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
                
    def get(self,key):
        # Insert your code here to get data by key
        hashvalue = self.hashfunction(key)
        print(hashvalue) #0..9
        self.slots[hashvalue] = key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)

# Store remaining input data
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
# H[89] = 'G'
# H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52])