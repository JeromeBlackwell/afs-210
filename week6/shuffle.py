import random

def shuffle(values):
    
    # Loop over the range of indexes from 0 up to the length of the list:

    for i in range(len(values) -1):

        # Randomly pick an index to swap with:

        indexChange = random.randint(0, len(values) -1)

        # Swap the values between the two indexes:

        values[i], values[indexChange] = values[indexChange], values[i]

    return values #return values

my_numbers = [27, 67, 45, 2, 79, 31, 98, 10, 59, 13]#test on random numbers
my_schedule= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]#test on random strings
print(shuffle(my_numbers))
print(shuffle(my_schedule))


#Time complexity is: 0(n) - The Time Complexity of a loop is considered as O(n) since the iterations of the function grow with the size of the list.